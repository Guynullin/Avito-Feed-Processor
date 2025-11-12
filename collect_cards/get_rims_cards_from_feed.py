import logging
import requests

from typing import List, Dict, Optional, Union
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from .cards_utils import construct_full_url
from .set_photo import set_photo
from xlsx_api.format_title import generate_rims_title
from .brand_model_filter_utils import match_rim_brand_and_model, load_allowed_rim_brands_and_models

skip_id_list = [632926]

def has_positive_rest(card):
    rest_keys = ["rest_count_kazan", "rest_count_kzn_dorozh", 
                "rest_count_samara", "rest_count_msk", "rest_count_ufa"]
    return any(card.get(key, 0) > 0 for key in rest_keys)

def try_parse_int(val):
    try:
        int_val = int(val)
        return int_val
    except Exception:
        return None

def try_parse_float(val):
    try:
        float_val = float(val)
        return float_val
    except Exception:
        return None

def check_dia(in_dia):
    float_dia = try_parse_float(in_dia)
    if float_dia is not None:
        if float_dia == 51.7:
            dia = 52
        elif float_dia == 130.8:
            dia = 131
        elif float_dia == 66.3:
            dia = 66.2
        elif float_dia == 124.3:
            dia = 125
        elif float_dia == 112.5:
            dia = 112
        elif float_dia == 69.6:
            dia = 70
        elif float_dia == 95.2:
            dia = 95.3
        elif float_dia == 66.66:
            dia = 66.6
        elif float_dia == 66.58:
            dia = 66.56
        elif float_dia == 62.6:
            dia = 62.5
        elif float_dia == 58.4:
            dia = 58.5
        else:
            dia = float_dia
        return dia
    else:
        return None

def check_bolts(in_bolts):
    int_bolts = try_parse_int(in_bolts)
    if int_bolts is not None:
        if int_bolts == 135:
            bolts = 8
        elif int_bolts == 127:
            bolts = 5
        else:
            bolts = int_bolts
        return bolts
    else:
        return None

def check_width(in_width):
    float_width = try_parse_float(in_width)
    if float_width is not None:
        if float_width == 8.75:
            width = 8.5
        elif float_width == 7.25:
            width = 7.5
        else:
            width = float_width
        return width
    else:
        return None

def check_pcd(in_pcd):
    float_pcd = try_parse_float(in_pcd)
    if float_pcd is not None:
        if float_pcd == 113:
            pcd = 112
        elif float_pcd == 112.5:
            pcd = 112
        elif float_pcd == 114.312:
            pcd = 114.3 
        else:
            pcd = float_pcd
        
        if isinstance(pcd, float) and pcd.is_integer():
            return int(pcd)
        else:
            return pcd
    else:
        return None

def add_to_card_if_not_none(card, key, value):
    if value is not None:
        card[key] = value

def create_session(retries: int = 5, backoff_factor: float = 0.3,
                  status_forcelist: List[int] = [500, 502, 503, 504]) -> requests.Session:
    """
    Creates a requests Session with retry strategy.

    :param retries: Maximum number of retries.
    :param backoff_factor: A backoff factor to apply between attempts.
    :param status_forcelist: A set of HTTP status codes to retry on.
    :return: Configured requests Session.
    """
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        method_whitelist=["GET"]
        # allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def is_xml_complete(content: bytes, chunk_size=1024) -> bool:
    """
    Checks if the XML feed is complete by analyzing the last chunk_size bytes.

    :param content: XML content as bytes.
    :param chunk_size: Number of bytes to check from the end of the file.
    :return: True if the XML is complete, otherwise False.
    """
    last_chunk = content[-chunk_size:]
    return "</products>" in last_chunk.decode("utf-8", errors="ignore")


def get_products_from_xml_feed(content: bytes, tag: str) -> List[BeautifulSoup]:
    """
    Parses XML content and extracts all product elements.

    :param content: XML content as bytes.
    :param tag: name of tag.
    :return: List of product BeautifulSoup objects.
    """
    soup = BeautifulSoup(content, 'xml')
    return soup.find_all(tag)


def extract_price(product: BeautifulSoup, tag: str) -> float:
    """
    Extracts and converts price from a given tag. Returns None if tag is missing or invalid.

    :param product: BeautifulSoup object of a product.
    :param tag: Tag name to extract the price from.
    :return: Price as int or None.
    """
    price_tag = product.find(tag)
    if price_tag and price_tag.text.strip().replace('.', '', 1).isdigit():
        try:
            return int(float(price_tag.text.strip()))
        except ValueError:
            pass
    return None

def extract_tag_data(product: BeautifulSoup, tag_name: str) -> float:
    """
    Extracts data from a given tag. Returns 0 if tag is missing or invalid.

    :param product: BeautifulSoup object of a product.
    :param tag: Tag name to extract the data.
    :return: str or 0.
    """
    tag = product.find(tag_name)
    if tag:
        return tag.text.strip()
    return None

def extract_pics(
    product: BeautifulSoup, 
    tag_name: str, 
    root_url: str, 
) -> Dict[str, Union[List[str], str]]:
    """
    Extracts picture URLs from a given tag within a product.

    :param product: The BeautifulSoup product element.
    :param tag_name: The name of the tag containing pictures.
    :param root_url: The root URL to prepend to picture paths.
    :return: A dictionary with the extracted picture URLs.
    """
    pics_data = {}
    tag = product.find(tag_name)
    if tag:
        pic_tags = tag.find_all("pic")
        if pic_tags:
            pic_list = [construct_full_url(root_url, pic.text.strip()) for pic in pic_tags if pic.text.strip()]
            pic_list = [url for url in pic_list if url]
            if pic_list:
                pics_data[tag_name] = pic_list
        else:
            pic_text = tag.text.strip()
            if pic_text:
                full_url = construct_full_url(root_url, pic_text)
                if full_url:
                    pics_data[tag_name] = full_url
    return pics_data



def get_rims_cards_from_feed(url: str,
                        url_moscow: str,
                        root_url: str,
                        url_portfolio: str,
                        headers: Dict[str, str]) -> Dict:
    """
    Retrieves and processes product cards from primary and Moscow XML feeds.

    :param url: URL of the primary XML feed.
    :param url_moscow: URL of the Moscow XML feed.
    :param root_url: Root URL for constructing full image URLs.
    :param url_portfolio: URL of the portfolio XML feed.
    :param headers: Dictionary containing request headers.
    :return: A dict with alloy/forged product card dictionaries or raise Exception.
    """
    session = create_session()
    alloy_cards = []
    forged_cards = []
    portfolio_cards = []
    alloy_titles = {}
    forged_titles = {}
    portfolio_titles = {}

    try:

        allowed_rims_models = load_allowed_rim_brands_and_models(session=session, headers=headers)
        if allowed_rims_models is None:
            logging.error(f"<get_rims_cards_from_feed> allowed_rims_models is None")
            raise Exception(f"<get_rims_cards_from_feed> allowed_rims_models is None")

        # Fetch primary feed
        response_primary = session.get(url, headers=headers, timeout=120)
        response_primary.raise_for_status()
        if is_xml_complete(response_primary.content):
            products_primary = get_products_from_xml_feed(response_primary.content, 'product')
        else:
            logging.error("<get_rims_cards_from_feed> XML feed is incomplete.")
            return {}

        # Fetch Moscow feed
        response_moscow = session.get(url_moscow, headers=headers, timeout=120)
        response_moscow.raise_for_status()
        products_moscow = get_products_from_xml_feed(response_moscow.content, 'product')

        # Fetch portfolio feed
        response_portfolio = session.get(url_portfolio, headers=headers, timeout=120)
        response_portfolio.raise_for_status()
        products_portfolio = get_products_from_xml_feed(response_portfolio.content, 'portfolio')

    except requests.RequestException as e:
        logging.error(f"<get_rims_cards_from_feed> Failed to fetch feeds: {e}")
        return {}

    # Create a mapping from product ID to Moscow prices
    moscow_prices = {}
    for product in products_moscow:
        product_id_tag = product.find("id")
        if product_id_tag and product_id_tag.text.strip().isdigit():
            pid = int(product_id_tag.text.strip())
            moscow_prices[pid] = {
                "price_origin_msk": extract_price(product, "price_origin"),
                "online_price_msk": extract_price(product, "online_price"),
                "promo_price_msk": extract_price(product, "promo_price"),
                "market_price_msk": extract_price(product, "market_price")
            }

    # Create a set of portfolio product IDs for quick lookup
    portfolio_ids = set()
    for product in products_portfolio:
        product_id_tag = product.find("id")
        if product_id_tag and product_id_tag.text.strip().isdigit():
            portfolio_ids.add(int(product_id_tag.text.strip()))

    for product in products_primary:
        product_id_tag = product.find("id")
        if not product_id_tag or not product_id_tag.text.strip().isdigit():
            continue
        product_id = int(product_id_tag.text.strip())

        if product_id in skip_id_list:
            continue

        # Determine if this is a portfolio product
        is_portfolio = product_id in portfolio_ids

        card = {
            "id": product_id,
            "rim_brand": "Default",
            "online_price": extract_price(product, "online_price"),
            "price_origin": extract_price(product, "price_origin"),
            "promo_price": extract_price(product, "promo_price"),
            "market_price": extract_price(product, "market_price"),
            "price_origin_msk": None,
            "online_price_msk": None,
            "promo_price_msk": None,
            "market_price_msk": None,
            "portfolio": is_portfolio
        }

        add_to_card_if_not_none(card, 'feed_title', extract_tag_data(product,'title'))
        input_brand_prim = extract_tag_data(product,'brand')
        input_model_prim = extract_tag_data(product,'model')
        brand_prim, model_prim = match_rim_brand_and_model(valid_brands_models=allowed_rims_models,
                                                 input_brand=input_brand_prim,
                                                 input_model=input_model_prim)
        add_to_card_if_not_none(card, 'RimBrand', brand_prim)
        add_to_card_if_not_none(card, 'RimModel', model_prim)
        add_to_card_if_not_none(card, 'brand', input_brand_prim)
        add_to_card_if_not_none(card, 'model', input_model_prim)
        add_to_card_if_not_none(card, 'articul', extract_tag_data(product,'articul'))
        add_to_card_if_not_none(card, 'rest_kazan', try_parse_int(extract_tag_data(product,'rest_count_kazan')))
        add_to_card_if_not_none(card, 'rest_ufa', try_parse_int(extract_tag_data(product,'rest_count_ufa')))
        add_to_card_if_not_none(card, 'dorozh', try_parse_int(extract_tag_data(product,'rest_count_kzn_dorozh')))
        add_to_card_if_not_none(card, 'type', extract_tag_data(product,'subtype'))
        add_to_card_if_not_none(card, 'diameter', try_parse_int(extract_tag_data(product,'diameter')))
        add_to_card_if_not_none(card, 'et', try_parse_float(extract_tag_data(product,'et_length')))
        add_to_card_if_not_none(card, 'width', check_width(extract_tag_data(product,'width')))
        add_to_card_if_not_none(card, 'pcd', check_pcd(extract_tag_data(product,'pcd')))
        add_to_card_if_not_none(card, 'bolts', check_bolts(extract_tag_data(product,'bolts')))
        add_to_card_if_not_none(card, 'dia', check_dia(extract_tag_data(product,'dia')))
        add_to_card_if_not_none(card, 'color', extract_tag_data(product,'color'))
        add_to_card_if_not_none(card, 'dia2', check_dia(extract_tag_data(product,'dia2')))
        add_to_card_if_not_none(card, 'et2', check_dia(extract_tag_data(product,'et_length2')))
        add_to_card_if_not_none(card, 'width2', check_dia(extract_tag_data(product,'width2')))
        add_to_card_if_not_none(card, 'pcd2', check_dia(extract_tag_data(product,'pcd2')))
        add_to_card_if_not_none(card, 'bolts2', check_dia(extract_tag_data(product,'bolts2')))
        add_to_card_if_not_none(card, 'rest_count_kazan', try_parse_int(extract_tag_data(product,'rest_count_kazan')))
        add_to_card_if_not_none(card, 'rest_count_kzn_dorozh', try_parse_int(extract_tag_data(product,'rest_count_kzn_dorozh')))
        add_to_card_if_not_none(card, 'rest_count_samara', try_parse_int(extract_tag_data(product,'rest_count_samara')))
        add_to_card_if_not_none(card, 'rest_count_msk', try_parse_int(extract_tag_data(product,'rest_count_msk')))
        add_to_card_if_not_none(card, 'rest_count_ufa', try_parse_int(extract_tag_data(product,'rest_count_ufa')))


        # Extract optional image fields
        card.update(extract_pics(product, "main_pic", root_url))
        card.update(extract_pics(product, "real_pics", root_url))
        # card.update(extract_pics(product, "bottom_slides", root_url))
        card.update(extract_pics(product, "additional_pics", root_url))
        set_photo(card)

        # Assign Moscow prices if available
        moscow_data = moscow_prices.get(product_id, {})
        card["price_origin_msk"] = moscow_data.get("price_origin_msk", None)
        card["online_price_msk"] = moscow_data.get("online_price_msk", None)
        card["promo_price_msk"] = moscow_data.get("promo_price_msk", None)
        card["market_price_msk"] = moscow_data.get("market_price_msk", None)
        
        if not 'main_pic' in card:
            logging.debug(f"no main_pic: {card}")
        if not 'price_origin' in card or card["price_origin"] is None or not card["price_origin"] > 0:
            logging.debug(f"no price_origin: {card}")
            continue
        if not 'feed_title' in card:
            logging.debug(f"no feed_title: {card}")
        if not 'brand' in card:
            logging.debug(f"no brand: {card}")
        if not 'model' in card:
            logging.debug(f"no model: {card}")
        if not 'diameter' in card:
            logging.debug(f"no diameter: {card}")
        if not 'et' in card:
            logging.debug(f"no et: {card}")
        if not 'width' in card:
            logging.debug(f"no width: {card}")
        if not 'pcd' in card:
            logging.debug(f"no pcd: {card}")
        if not 'bolts' in card:
            logging.debug(f"no bolts: {card}")
        if not 'dia' in card:
            logging.debug(f"no dia: {card}")
        if not 'type' in card:
            logging.debug(f"no type: {card}")


        if 'main_pic' in card and\
            'price_origin' in card and\
            card['price_origin'] > 0 and\
            'feed_title' in card and\
            'brand' in card and\
            'diameter' in card and\
            'et' in card and\
            'width' in card and\
            'pcd' in card and\
            'bolts' in card and\
            'dia' in card and\
            'type' in card:

            title = generate_rims_title(card)
            if title is not None:
                card['title'] = title
                if card['type'] == 'alloy' or card['type'] == 'flow_forming':
                    if title in alloy_titles:
                        alloy_titles[title] += 1
                    else:
                        alloy_titles[title] = 1
                    alloy_cards.append(card)
                elif card['type'] == 'forged':
                    if title in forged_titles:
                        forged_titles[title] += 1
                    else:
                        forged_titles[title] = 1
                    forged_cards.append(card)
        
    portfolio_count = 0
    for product in products_portfolio:
        product_id_tag = product.find("id")
        if not product_id_tag or not product_id_tag.text.strip().isdigit():
            continue
        product_id = int(product_id_tag.text.strip())

        card = {
            "id": product_id,
            "rim_brand": "Default",
            "online_price": extract_price(product, "online_price"),
            "price_origin": extract_price(product, "price_origin"),
            "promo_price": extract_price(product, "promo_price"),
            "market_price": extract_price(product, "market_price"),
            "price_origin_msk": None,
            "online_price_msk": None,
            "promo_price_msk": None,
            "market_price_msk": None,
            "portfolio": True  
        }

        add_to_card_if_not_none(card, 'feed_title', extract_tag_data(product,'title'))
        input_brand_port = extract_tag_data(product,'brand')
        input_model_port = extract_tag_data(product,'model')
        brand_port, model_port = match_rim_brand_and_model(valid_brands_models=allowed_rims_models,
                                                 input_brand=input_brand_port,
                                                 input_model=input_model_port)
        add_to_card_if_not_none(card, 'RimBrand', brand_port)
        add_to_card_if_not_none(card, 'RimModel', model_port)
        add_to_card_if_not_none(card, 'brand', input_brand_port)
        add_to_card_if_not_none(card, 'model', input_model_port)
        add_to_card_if_not_none(card, 'articul', extract_tag_data(product,'articul'))
        add_to_card_if_not_none(card, 'rest_kazan', try_parse_int(extract_tag_data(product,'rest_count_kazan')))
        add_to_card_if_not_none(card, 'rest_ufa', try_parse_int(extract_tag_data(product,'rest_count_ufa')))
        add_to_card_if_not_none(card, 'dorozh', try_parse_int(extract_tag_data(product,'rest_count_kzn_dorozh')))
        add_to_card_if_not_none(card, 'type', extract_tag_data(product,'subtype'))
        add_to_card_if_not_none(card, 'diameter', try_parse_int(extract_tag_data(product,'diameter')))
        add_to_card_if_not_none(card, 'et', try_parse_float(extract_tag_data(product,'et_length')))
        add_to_card_if_not_none(card, 'width', check_width(extract_tag_data(product,'width')))
        add_to_card_if_not_none(card, 'pcd', check_pcd(extract_tag_data(product,'pcd')))
        add_to_card_if_not_none(card, 'bolts', check_bolts(extract_tag_data(product,'bolts')))
        add_to_card_if_not_none(card, 'dia', check_dia(extract_tag_data(product,'dia')))
        add_to_card_if_not_none(card, 'color', extract_tag_data(product,'color'))
        add_to_card_if_not_none(card, 'dia2', check_dia(extract_tag_data(product,'dia2')))
        add_to_card_if_not_none(card, 'et2', check_dia(extract_tag_data(product,'et_length2')))
        add_to_card_if_not_none(card, 'width2', check_dia(extract_tag_data(product,'width2')))
        add_to_card_if_not_none(card, 'pcd2', check_dia(extract_tag_data(product,'pcd2')))
        add_to_card_if_not_none(card, 'bolts2', check_dia(extract_tag_data(product,'bolts2')))
        add_to_card_if_not_none(card, 'rest_count_kazan', try_parse_int(extract_tag_data(product,'rest_count_kazan')))
        add_to_card_if_not_none(card, 'rest_count_kzn_dorozh', try_parse_int(extract_tag_data(product,'rest_count_kzn_dorozh')))
        add_to_card_if_not_none(card, 'rest_count_samara', try_parse_int(extract_tag_data(product,'rest_count_samara')))
        add_to_card_if_not_none(card, 'rest_count_msk', try_parse_int(extract_tag_data(product,'rest_count_msk')))
        add_to_card_if_not_none(card, 'rest_count_ufa', try_parse_int(extract_tag_data(product,'rest_count_ufa')))

        card.update(extract_pics(product, "main_pic", root_url))
        card.update(extract_pics(product, "real_pics", root_url))
        # card.update(extract_pics(product, "bottom_slides", root_url))
        card.update(extract_pics(product, "additional_pics", root_url))
        set_photo(card)

        if ('main_pic' in card and
            'price_origin' in card and
            card['price_origin'] > 0 and
            'feed_title' in card and
            'brand' in card and
            'diameter' in card and
            'et' in card and
            'width' in card and
            'pcd' in card and
            'bolts' in card and
            'dia' in card and
            'type' in card):

            if 'feed_title' in card and isinstance(card['feed_title'], str) and len(card['feed_title']) > 10:
                title = card['feed_title']
            else:
                title = generate_rims_title(card)
            if title is not None:
                card['title'] = title
                if card['type'] == 'alloy' or card['type'] == 'flow_forming':
                    if title in alloy_titles:
                        alloy_titles[title] += 1
                    else:
                        alloy_titles[title] = 1
                    portfolio_count += 1
                    alloy_cards.append(card)
                elif card['type'] == 'forged':
                    if title in forged_titles:
                        forged_titles[title] += 1
                    else:
                        forged_titles[title] = 1
                    portfolio_count += 1
                    forged_cards.append(card)

    if len(alloy_cards) > 0 and len(forged_cards) > 0:
        filtered_alloy_cards_list = [card for card in alloy_cards 
            if alloy_titles[card['title']] == 1 or has_positive_rest(card)]
    
        filtered_forged_cards_list = [card for card in forged_cards 
            if forged_titles[card['title']] == 1 or has_positive_rest(card)]
        # filtered_alloy_cards_list = [card for card in alloy_cards if alloy_titles[card['title']] == 1]
        # filtered_forged_cards_list = [card for card in forged_cards if forged_titles[card['title']] == 1]
        return {'alloy' : filtered_alloy_cards_list, 'forged' : filtered_forged_cards_list}
    else:
        raise Exception(f"<get_rims_cards_from_feed> empty list, len(alloy_cards): {len(alloy_cards)}, len(forged_cards): {len(forged_cards)}")
    


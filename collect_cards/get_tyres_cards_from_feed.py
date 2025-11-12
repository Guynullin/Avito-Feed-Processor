import logging
import requests

from typing import List, Dict, Optional, Union
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
from .get_brands_models_avito import get_avito_tyre_brands
from .cards_utils import construct_full_url
from .set_photo import set_photo
from xlsx_api.format_title import generate_tyres_title
from config import TYRES_LIST

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

def similar(db: str, avito: str, p_ratio: float):
    """compares incoming rows by ratio.

    :param db: a string from database.
    :param avito: a string from avito xml.
    :param p_ratio: ratio.
    :return: boolean value True or False.
    """
    db_model = db.lower()
    avito_model = avito.lower()
    ratio = SequenceMatcher(None, db_model, avito_model).ratio()

    if ratio > p_ratio:
        return True
    else:
        return False

def select_brand_model(db_brand, db_model: str, brands_avito: dict):
    """returns a dictionary with the brand and model 
    matching the data from avito xml.

    :param db_brand: a string with brand from database.
    :param db_model: a string with model from database.
    :param brands_avito: a list with brands from avito xml.
    :return: a dictionary with the brand and model from avito or
        a dictionary with the brand Nobrand and model Nomodel if no match.
    """
    card_brand = 'Nobrand'
    card_model = 'Nomodel'

    clear_model = db_model.replace('IV', '').replace('III', '').replace('SF-988', 'SF988')\
    .replace('EH 23', 'EH23').replace('5 STUDDED', '5').replace('ALL-TERRAIN A/T', 'All-Terrain T/A')\
    .replace('L-ZEAL 56','L-Zeal56').replace('CROCODILE M/T', 'CROCODILE').replace('(БЕЗ ШИПОВ)', '')\
    .replace('X-PRIVILO TX3', 'X-Privilo TX3').replace('WINTER I*PIKE RS 2 W429', "WINTER I'PIKE RS2").strip()

    if db_brand:
        if 'NOKIAN TYRES'.lower() in db_brand.lower():
            db_brand = 'Ikon Tyres'
        if 'KAMA'.lower() in db_brand.lower():
            db_brand = 'КАМА'
        if 'TORQUE TIRES'.lower() in db_brand.lower():
            db_brand = 'TORQUE'
        if 'TRI-ACE'.lower() in db_brand.lower():
            db_brand = 'Tri Ace'
        if 'RAZI TIRE'.lower() in db_brand.lower():
            db_brand = 'RAZI'
        if 'БАРНАУЛЬСКИЙ'.lower() in db_brand.lower():
            db_brand = 'Барнаул'
        if 'КИРОВСКИЙ'.lower() in db_brand.lower():
            db_brand = 'КШЗ'


        for key in brands_avito:
            if db_brand.lower() in key.lower():
                card_brand = key
                for av_model in brands_avito[key]:
                    if similar(clear_model, av_model, 0.9):
                        card_model = av_model                        
                        break
                if card_model == 'Nomodel':
                    for av_model in brands_avito[key]:
                        if similar(clear_model, av_model, 0.83):
                            card_model = av_model                        
                            break
                if card_model == 'Nomodel':
                    for av_model in brands_avito[key]:
                        if similar(clear_model, av_model, 0.56):
                            card_model = av_model                        
                            break
                break
            
    if card_brand != 'Nobrand' and card_model != 'Nomodel':
        return {'brand': card_brand, 'model' : card_model}
    else:
        return {}

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



def get_products_from_xml_feed(content: bytes) -> List[BeautifulSoup]:
    """
    Parses XML content and extracts all product elements.

    :param content: XML content as bytes.
    :return: List of product BeautifulSoup objects.
    """
    soup = BeautifulSoup(content, 'xml')
    return soup.find_all("product")


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



def get_tyres_cards_from_feed(url: str,
                        avito_url: str,
                        root_url: str,
                        headers: Dict[str, str]) -> Dict:
    """
    Retrieves and processes product cards from primary and Moscow XML feeds.

    :param url: URL of the primary XML feed.
    :param url_moscow: URL of the Moscow XML feed.
    :param root_url: Root URL for constructing full image URLs.
    :param headers: Dictionary containing request headers.
    :return: A dict with alloy/forged product card dictionaries or raise Exception.
    """
    session = create_session()
    summer_tyres = []
    summer_tyres_titles = {}

    try:
        avito_tyre_brands = get_avito_tyre_brands(avito_url)
        if avito_tyre_brands == 0:
            logging.error('<get_tyres_cards_from_feed> avito_tyre_brands is empty')
            return {}
        # Fetch primary feed
        response_primary = session.get(url, headers=headers, timeout=120)
        response_primary.raise_for_status()
        if is_xml_complete(response_primary.content):
            products_primary = get_products_from_xml_feed(response_primary.content)
        else:
            logging.error("<get_tyres_cards_from_feed> XML feed is incomplete.")
            return {}

        # Fetch Moscow feed
        # response_moscow = session.get(url_moscow, headers=headers, timeout=120)
        # response_moscow.raise_for_status()
        # products_moscow = get_products_from_xml_feed(response_moscow.content)

    except requests.RequestException as e:
        logging.error(f"<get_tyres_cards_from_feed> Failed to fetch feeds: {e}")
        return {}

    # Create a mapping from product ID to Moscow prices
    # moscow_prices = {}
    # for product in products_moscow:
    #     product_id_tag = product.find("id")
    #     if product_id_tag and product_id_tag.text.strip().isdigit():
    #         pid = int(product_id_tag.text.strip())
    #         moscow_prices[pid] = {
    #             "price_origin_msk": extract_price(product, "price_origin"),
    #             "online_price_msk": extract_price(product, "online_price"),
    #             "promo_price_msk": extract_price(product, "promo_price"),
    #             "market_price_msk": extract_price(product, "market_price")
    #         }

    for product in products_primary:
        product_id_tag = product.find("id")
        if not product_id_tag or not product_id_tag.text.strip().isdigit():
            continue
        product_id = int(product_id_tag.text.strip())

        card = {
            "id": product_id,
            "online_price": extract_price(product, "online_price"),
            "price_origin": extract_price(product, "price_origin"),
            "promo_price": extract_price(product, "promo_price"),
            "market_price": extract_price(product, "market_price"),
            "price_origin_msk": None,
            "online_price_msk": None,
            "promo_price_msk": None,
            "market_price_msk": None
        }

        add_to_card_if_not_none(card, 'feed_title', extract_tag_data(product,'title'))
        add_to_card_if_not_none(card, 'brand', extract_tag_data(product,'brand'))
        add_to_card_if_not_none(card, 'model', extract_tag_data(product,'model'))
        add_to_card_if_not_none(card, 'articul', extract_tag_data(product,'articul'))
        # add_to_card_if_not_none(card, 'rest_kazan', try_parse_int(extract_tag_data(product,'rest_count_kazan')))
        # add_to_card_if_not_none(card, 'rest_ufa', try_parse_int(extract_tag_data(product,'rest_count_ufa')))
        # add_to_card_if_not_none(card, 'dorozh', try_parse_int(extract_tag_data(product,'rest_count_kzn_dorozh')))
        add_to_card_if_not_none(card, 'type', extract_tag_data(product,'type'))
        add_to_card_if_not_none(card, 'seasonality', extract_tag_data(product,'seasonality'))
        add_to_card_if_not_none(card, 'spikes', extract_tag_data(product,'spikes'))
        add_to_card_if_not_none(card, 'width', extract_tag_data(product,'width'))
        add_to_card_if_not_none(card, 'height', extract_tag_data(product,'height'))
        add_to_card_if_not_none(card, 'diameter', try_parse_int(extract_tag_data(product,'diameter')))
        add_to_card_if_not_none(card, 'suv', extract_tag_data(product,'suv'))
        add_to_card_if_not_none(card, 'load_index', extract_tag_data(product,'load_index'))
        add_to_card_if_not_none(card, 'speed_index', extract_tag_data(product,'speed_index'))
        add_to_card_if_not_none(card, 'runflat', extract_tag_data(product,'runflat'))


        # Extract optional image fields
        card.update(extract_pics(product, "main_pic", root_url))
        card.update(extract_pics(product, "real_pics", root_url))
        card.update(extract_pics(product, "bottom_slides", root_url))
        card.update(extract_pics(product, "additional_pics", root_url))
        set_photo(card)

        # Assign Moscow prices if available
        # moscow_data = moscow_prices.get(product_id, {})
        # card["price_origin_msk"] = moscow_data.get("price_origin_msk", None)
        # card["online_price_msk"] = moscow_data.get("online_price_msk", None)
        # card["promo_price_msk"] = moscow_data.get("promo_price_msk", None)
        # card["market_price_msk"] = moscow_data.get("market_price_msk", None)
        
        if not 'main_pic' in card:
            logging.warning(f"no main_pic: {card}")
            continue
        if not 'price_origin' in card or card["price_origin"] is None\
            or not card["price_origin"] > 0:
            logging.warning(f"no price_origin: {card}")
            continue
        if not 'feed_title' in card:
            logging.warning(f"no feed_title: {card}")
            continue
        if not 'brand' in card:
            logging.warning(f"no brand: {card}")
            continue
        if not 'model' in card:
            logging.warning(f"no model: {card}")
            continue
        if not 'diameter' in card:
            logging.warning(f"no diameter: {card}")
            continue
        if not 'type' in card:
            logging.warning(f"no type: {card}")
            continue
        if not 'seasonality' in card:
            logging.warning(f"no seasonality: {card}")
            continue
        if not 'spikes' in card:
            logging.warning(f"no spikes: {card}")
            continue
        if not 'width' in card:
            logging.warning(f"no width: {card}")
            continue
        if not 'height' in card:
            logging.warning(f"no height: {card}")
            continue
        if not 'suv' in card:
            logging.warning(f"no suv: {card}")
        if not 'load_index' in card:
            logging.warning(f"no load_index: {card}")
            continue
        if not 'speed_index' in card:
            logging.warning(f"no speed_index: {card}")
            continue
        if not 'runflat' in card:
            logging.warning(f"no runflat: {card}")
            continue
        else:
            if card['runflat'] == 'False':
                card['runflat'] = 'Нет'
            else:
                card['runflat'] = 'Да'
        

        if card['type'] == 'tire' and\
            card['seasonality'] == 'Летняя' and\
            card['spikes'] == 'False' and\
            card['brand'].lower() in TYRES_LIST and\
            'main_pic' in card and\
            'price_origin' in card and\
            card['price_origin'] > 0 and\
            'brand' in card and\
            'model' in card and\
            'diameter' in card and\
            'type' in card:

            brand_model_dict = select_brand_model(card['brand'], card['model'], avito_tyre_brands)
            if brand_model_dict:
                card['brand'] = brand_model_dict['brand']
                card['model'] = brand_model_dict['model']
                
                tire_type = card['seasonality'].replace('Летняя', 'Летние').replace('Зимняя', 'Зимние')\
                .replace('Всесезонная', 'Всесезонные')
                if card['spikes'] == 'True':
                    tire_type = f"{tire_type} шипованные"
                elif tire_type == 'Зимние':
                    tire_type = f"{tire_type} нешипованные"
                
                card['tire_type'] = tire_type

                if card['height'] == 0 or card['height'] == '0':
                    card['height'] = 5
                if card['height'] == 12 or card['height'] == '12':
                    card['height'] = 12.5

                title = generate_tyres_title(card)
                if title is not None:
                    card['title'] = title
                    if title in summer_tyres_titles:
                        summer_tyres_titles[title] += 1
                    else:
                        summer_tyres_titles[title] = 1
                    summer_tyres.append(card)
            

    if len(summer_tyres) > 0:
        filtered_summer_tyres_list = [card for card in summer_tyres if summer_tyres_titles[card['title']] == 1]
        return {'tires' : filtered_summer_tyres_list}
    else:
        raise Exception(f"<get_tyres_cards_from_feed> empty list, len(summer_tyres): {len(summer_tyres)}")
    


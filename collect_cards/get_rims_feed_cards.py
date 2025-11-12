import logging
import requests

from typing import List, Dict, Optional, Union
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from .cards_utils import construct_full_url



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
    Extracts and converts price from a given tag. Returns 0 if tag is missing or invalid.

    :param product: BeautifulSoup object of a product.
    :param tag: Tag name to extract the price from.
    :return: Price as int or 0.
    """
    price_tag = product.find(tag)
    if price_tag and price_tag.text.strip().replace('.', '', 1).isdigit():
        try:
            return int(float(price_tag.text.strip()))
        except ValueError:
            pass
    return 0


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


def get_rims_feed_cards(url: str, url_moscow: str, root_url: str,
                  headers: Dict[str, str], id_list: Optional[List[int]] = None) -> List[Dict]:
    """
    Retrieves and processes product cards from primary and Moscow XML feeds.

    :param url: URL of the primary XML feed.
    :param url_moscow: URL of the Moscow XML feed.
    :param root_url: Root URL for constructing full image URLs.
    :param headers: Dictionary containing request headers.
    :param id_list: List of product IDs to filter, defaults to None.
    :return: A list of product card dictionaries or an empty list if an error occurs.
    """
    session = create_session()
    cards_list = []

    try:
        # Fetch primary feed
        response_primary = session.get(url, headers=headers, timeout=120)
        response_primary.raise_for_status()
        products_primary = get_products_from_xml_feed(response_primary.content)

        # Fetch Moscow feed
        response_moscow = session.get(url_moscow, headers=headers, timeout=120)
        response_moscow.raise_for_status()
        products_moscow = get_products_from_xml_feed(response_moscow.content)

    except requests.RequestException as e:
        logging.error(f"<get_feed_cards> Failed to fetch feeds: {e}")
        return []

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

    for product in products_primary:
        product_id_tag = product.find("id")
        if not product_id_tag or not product_id_tag.text.strip().isdigit():
            continue
        product_id = int(product_id_tag.text.strip())

        if id_list is not None and product_id not in id_list:
            continue

        card = {
            "id": product_id,
            "online_price": extract_price(product, "online_price"),
            "price_origin": extract_price(product, "price_origin"),
            "promo_price": extract_price(product, "promo_price"),
            "market_price": extract_price(product, "market_price"),
            "price_origin_msk": 0,
            "online_price_msk": 0,
            "promo_price_msk": 0,
            "market_price_msk": 0
        }

        if product.find("brand"):
            card["feed_brand"] = product.find("brand").text
        if product.find("model"):
            card["feed_model"] = product.find("model").text
        if product.find("color"):
            card["feed_color"] = product.find("color").text

        # Extract optional image fields
        card.update(extract_pics(product, "main_pic", root_url))
        card.update(extract_pics(product, "real_pics", root_url))
        card.update(extract_pics(product, "bottom_slides", root_url))
        card.update(extract_pics(product, "additional_pics", root_url))

        # Assign Moscow prices if available
        moscow_data = moscow_prices.get(product_id, {})
        card["price_origin_msk"] = moscow_data.get("price_origin_msk", 0)
        card["online_price_msk"] = moscow_data.get("online_price_msk", 0)
        card["promo_price_msk"] = moscow_data.get("promo_price_msk", 0)
        card["market_price_msk"] = moscow_data.get("market_price_msk", 0)

        if 'main_pic' in card and 'price_origin' in card and card['price_origin'] > 0:
            cards_list.append(card)

    if cards_list:
        logging.info(f"<get_feed_cards> Retrieved {len(cards_list)} cards from {url}")
    else:
        logging.error(f"<get_feed_cards> No cards retrieved from {url}")

    return cards_list


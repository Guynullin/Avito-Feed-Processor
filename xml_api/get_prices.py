import logging
from typing import Optional, Dict, Union


def get_alloy_price(card: dict, tag: str) -> Optional[int]:
    """
    Retrieves the alloy price from a product card.

    :param card: A dictionary representing the product card.
    :param tag: A string tag.
    :return: The alloy price as an integer if found and valid, otherwise None.
    """
    try:
        tag_price = card.get(tag)
        if tag_price is not None:
            tag_price_int = int(tag_price)
            if tag_price_int > 0:
                logging.debug(f"<get_alloy_price> Retrieved '{tag}': {tag_price_int}")
                return tag_price_int
            else:
                logging.debug(f"<get_alloy_price> '{tag}' is not greater than 0: {tag_price_int}")
    except (ValueError, TypeError) as e:
        logging.debug(f"<get_alloy_price> Error converting '{tag}' to int: {e}")

    logging.debug("<get_alloy_price> No valid alloy price found.")
    return None

def get_moscow_alloy_price(card: dict, tag: str) -> Optional[Dict[str, Union[int, bool]]]:
    """
    Retrieves the Moscow alloy price from a product card.

    :param card: A dictionary representing the product card.
    :param tag: A string tag.
    :return: The dictionary with Moscow alloy price as an integer if found and valid, otherwise None.
    """
    # Attempt to retrieve tag
    try:
        tag_price = card.get(tag)
        if tag_price is not None:
            tag_price_int = int(tag_price)
            if tag_price_int > 0:
                logging.debug(f"<get_moscow_alloy_price> Retrieved '{tag}': {tag_price_int}")
                return {"price" : tag_price_int, "is_origin" : False}
            else:
                logging.debug(f"<get_moscow_alloy_price> '{tag}' is not greater than 0: {tag_price_int}")
    except (ValueError, TypeError) as e:
        logging.debug(f"<get_moscow_alloy_price> Error converting '{tag}' to int: {e}")

    # Attempt to retrieve 'price_origin_msk'
    try:
        price_origin_msk = card.get("price_origin_msk")
        if price_origin_msk is not None:
            price_origin_msk_int = int(price_origin_msk)
            if price_origin_msk_int > 0:
                logging.debug(f"<get_moscow_alloy_price> Retrieved 'price_origin_msk': {price_origin_msk_int}")
                return {"price" : price_origin_msk_int, "is_origin" : True}
            else:
                logging.debug(f"<get_moscow_alloy_price> 'price_origin_msk' is not greater than 0: {price_origin_msk_int}")
    except (ValueError, TypeError) as e:
        logging.debug(f"<get_moscow_alloy_price> Error converting 'price_origin_msk' to int: {e}")

    logging.debug("<get_moscow_alloy_price> No valid Moscow alloy price found.")
    return None

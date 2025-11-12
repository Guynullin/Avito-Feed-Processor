import logging

from .get_image_dict import get_image_dict
from .get_feed_cards import get_feed_cards
from .set_price_and_photo import set_price_and_photo
from config import URL_DICT

def get_tires_list(db_list: list):
    """Reads 'Лист загрузки шин' sheet and returns a list
    containing only the cards necessary for recording.

    :param db_list: a tire cards from db.
    :return: a list with the tire cards or 0 if error occured.
    """
    tire_id_list = []
    cards_list = []
    tire_slugs = []

    if len(db_list) > 0:
        for item in db_list:
            tire_id_list.append(item["id"])
            tire_slugs.append(item["slug"])
    else:
        return 0
    
    if len(tire_slugs) > 0:
        image_dict = get_image_dict(sitemap_url=URL_DICT["url_tyres_sitemap"], slugs_list=tire_slugs)
    if len(tire_id_list) > 0:
        feed_cards = get_feed_cards(url=URL_DICT["tyres_url"], root_url=URL_DICT["root_url"],\
            headers=URL_DICT["headers"], id_list=tire_id_list)
    # set photo and price to cards from db
    for card in db_list:
        set_price_and_photo(card=card,\
                    image_dict=image_dict, feed_cards=feed_cards, type="tires")
        if not card["photo"] is None:
            cards_list.append(card)
    del image_dict
    del feed_cards

    if len(cards_list) > 0:
        logging.info(f"<get_tires_list> tyres cards: {len(cards_list)}")
        return cards_list
    else:
        logging.error(f"<get_tires_list> cards_list is empty, return 0")
        return 0
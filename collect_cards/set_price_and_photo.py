import random
import logging

from config import URL_DICT, RIM_DIAMETER_LIST

def set_price_and_photo(card: dict, image_dict: dict, feed_cards: list, type: str = None,\
        rim_diameter = None) -> None:
    """Setting price and images to card.

    :param card: a product card.
    :param image_dict: dictionary containing a products slug and 
        a corresponding list of links to images.
    :param feed_cards: a list with product cards from feed.
    :param rim_diameter: the value of the disc diameter from the card, defaults is None.
    :return: None.
    """

    if type == "alloy" and "ad_photo_1" in URL_DICT:
        if rim_diameter and rim_diameter in RIM_DIAMETER_LIST:
            ad_list = [
                URL_DICT["ad_photo_1"],
                URL_DICT["ad_photo_1"]
            ]
        else:
            ad_list = [
                URL_DICT["ad_photo_1"],
                URL_DICT["ad_photo_1"]
            ]
    elif type == "forged" and "ad_photo_5" in URL_DICT:
        ad_list = [
            URL_DICT["ad_photo_6"],
            URL_DICT["ad_photo_6"]
        ]
    elif type == "tires" and "ad_photo_6" in URL_DICT:
        ad_list = [
            URL_DICT["ad_photo_6"],
            URL_DICT["ad_photo_6"]
        ]
    else:
        ad_list = [
            URL_DICT["ad_photo_1"],
            URL_DICT["ad_photo_1"]
        ]
    image_list = []
    try:
        for feed in feed_cards:
            if str(feed["id"]) == str(card["id"]):
                if "feed_brand" in feed:
                    card["feed_brand"] = feed["feed_brand"]
                if "feed_model" in feed:
                    card["feed_model"] = feed["feed_model"]
                if "feed_color" in feed:
                    card["feed_color"] = feed["feed_color"]
                # set price
                if "price_origin" in feed and not feed["price_origin"] is None:
                    card["price"] = int(feed["price_origin"])
                if 'market_price' in feed:
                    card['market_price'] = feed['market_price']
                if 'promo_price' in feed:
                    card['promo_price'] = feed['promo_price']
                if 'price_origin_msk' in feed:
                    card['price_origin_msk'] = feed['price_origin_msk']
                if 'market_price_msk' in feed:
                    card['market_price_msk'] = feed['market_price_msk']
                if 'promo_price_msk' in feed:
                    card['promo_price_msk'] = feed['promo_price_msk']
                # set photo
                if "bottom_slides" in feed and isinstance(feed["bottom_slides"], list):
                    image_list += feed["bottom_slides"]
                if "real_pics" in feed and isinstance(feed["real_pics"], list):
                    image_list += feed["real_pics"]
                    # card["real_pics"] = feed["real_pics"]
                if "additional_pics" in feed and isinstance(feed["additional_pics"], list):
                    image_list += feed["additional_pics"]
                if "main_pic" in feed and isinstance(feed["main_pic"], str):
                    image_list.append(feed["main_pic"])
                
        # set photo alternative
        if len(image_list) == 0:
            if "slug" in card and card["slug"] in image_dict and isinstance(image_dict[card["slug"]], list):
                url_list = image_dict[card["slug"]]
                if len(url_list) > 3:
                    lst1 = url_list[3:]
                    lst2 = url_list[:3]
                    image_list = lst1 + lst2
                else:
                    image_list = url_list
                
        if len(image_list) > 0:
            if ad_list:
                image_list.insert(1, random.choice(ad_list))
            image_list = [url.strip() for url in image_list]
            result = '|'.join(image_list[:10])
            card["photo"] = result
            return
        else:
            card["photo"] = None
            return 

    except Exception as e:
        logging.error(f"<set_price_and_photo> {e}, set single ad_photo")
        card["photo"] = None
        return 

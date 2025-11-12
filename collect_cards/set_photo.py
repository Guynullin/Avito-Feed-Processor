import random
import logging

from config import URL_DICT, RIM_DIAMETER_LIST

def set_photo(card: dict) -> None:
    """Setting images to card.

    :param card: a product card.
    :return: None.
    """
    if not 'type' in card or not 'diameter' in card:
        return
    

    if (card['type'] == "alloy" or card['type'] == "flow_forming") and "ad_photo_1" in URL_DICT:
        if card['diameter'] in RIM_DIAMETER_LIST:
            ad_list = [
                URL_DICT["ad_photo_1"],
                URL_DICT["ad_photo_1"]
            ]
        else:
            ad_list = [
                URL_DICT["ad_photo_1"],
                URL_DICT["ad_photo_1"]
            ]
    elif card['type'] == "forged" and "ad_photo_5" in URL_DICT:
        ad_list = [
            URL_DICT["ad_photo_5"],
            URL_DICT["ad_photo_5"]
        ]
    elif card['type'] == "tires" and "ad_photo_6" in URL_DICT:
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

        # if "bottom_slides" in card and card["bottom_slides"]:
        #     image_list += [card["bottom_slides"]] if isinstance(card["bottom_slides"], str) else card["bottom_slides"]
        if "real_pics" in card and card["real_pics"]:
            image_list += [card["real_pics"]] if isinstance(card["real_pics"], str) else card["real_pics"] 
        if "additional_pics" in card and card["additional_pics"]:
            image_list += [card["additional_pics"]] if isinstance(card["additional_pics"], str) else card["additional_pics"]
        if "main_pic" in card and card["main_pic"]:
            image_list += [card["main_pic"]] if isinstance(card["main_pic"], str) else card["main_pic"]
            
                
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

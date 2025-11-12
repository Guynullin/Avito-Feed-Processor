import logging
import requests

from bs4 import BeautifulSoup

def get_feed_cards(url: str, root_url: str, headers: dict, id_list:list=None):
    """returns a list containing product cards from client's feed.

    :param url: a feed url.
    :param root_url: a root client's website.
    :param headers: a dictionary with requst headers.
    :param id_list: a list with product cards id, defaults in None.
    :return: a list with prod cards or empty list if error occured.
    """
    cards_list = []
    err_count = 0
    while True:

        if err_count >= 10:
            logging.error(f"<get_feed_cards> err_count >= 10")
            break

        try:
            resp = requests.get(url=url, headers=headers)

            if resp.status_code == 200:

                soup = BeautifulSoup(resp.content, 'xml')

                product_list = soup.find_all("product")

                if len(product_list) > 0:
                    for product in product_list:
                        card = {}
                        if product.find("id"):
                            card["id"] = product.find("id").text
                        else:
                            continue
                        if product.find("brand"):
                            card["feed_brand"] = product.find("brand").text
                        if product.find("model"):
                            card["feed_model"] = product.find("model").text
                        if product.find("color"):
                            card["feed_color"] = product.find("color").text
                        if product.find("online_price"):
                            card["online_price"] = product.find("online_price").text
                        else:
                            continue
                        if product.find("price_origin"):
                            card["price_origin"] = product.find("price_origin").text
                        else:
                            continue
                        if product.find("main_pic"):
                            card["main_pic"] = root_url + product.find("main_pic").text.strip()
                        if product.find("real_pics"):
                            real_pics = product.find("real_pics")
                            if len(real_pics.find_all("pic")) > 0:
                                pic_list = real_pics.find_all("pic")
                                real_pics_list = []
                                for item in pic_list:
                                    real_pics_list.append(root_url + item.text.strip())
                                if len(real_pics_list) > 0:
                                    card["real_pics"] = real_pics_list
                        if product.find("bottom_slides"):
                            bottom_slides = product.find("bottom_slides")
                            if len(bottom_slides.find_all("pic")) > 0:
                                pic_list = bottom_slides.find_all("pic")
                                bottom_slides_list = []
                                for item in pic_list:
                                    bottom_slides_list.append(root_url + item.text.strip())
                                if len(bottom_slides_list) > 0:
                                    card["bottom_slides"] = bottom_slides_list
                        if product.find("additional_pics"):
                            additional_pics = product.find("additional_pics")
                            if len(additional_pics.find_all("pic")) > 0:
                                pic_list = additional_pics.find_all("pic")
                                additional_pics_list = []
                                for item in pic_list:
                                    additional_pics_list.append(root_url + item.text.strip())
                                if len(additional_pics_list) > 0:
                                    card["additional_pics"] = additional_pics_list
                        if not id_list is None:
                            if int(card["id"]) in id_list:
                                cards_list.append(card)
                        else:
                            cards_list.append(card)
                    break
                else:
                    logging.warning(f"<get_feed_cards> product_list is empty")
                    err_count += 1
            else:
                logging.warning(f"<get_feed_cards> status: {resp.status_code}")
                err_count += 1
        except Exception as e:
            err_count += 1
            logging.warning(f"<get_feed_cards> exception: {e}")

    if len(cards_list) > 0:
        logging.info(f"<get_feed_cards> cards: {len(cards_list)} for {url}")
        return cards_list
    else:
        logging.error(f"<get_feed_cards> cards_list is empty for {url}")
        return []
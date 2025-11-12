import logging

from info_bot import send_message
from config import TYRE_DIAMETRES, TYRE_BRANDS
from .get_tires_list import get_tires_list
from .get_brands_models_avito import get_avito_tyre_brands
from .parse_rim import parse_rim
from .parse_tire import parse_tire
from .parse_input_tire import get_input_tire_strings
from .get_image_dict import get_image_dict
from .get_rims_feed_cards import get_rims_feed_cards

def get_cards_from_db(conn, url_dict, input_file_path: str, input_filename: str):
    """Returns a dictionary containing product cards from database.

    :param conn: a database connection.
    :param url_dict: a dictionary with url data.
    :param input_file_path: a path to the input file directory .
    :param input_filename: a name of input file.
    :return: dictionary with product cards.
    """
    with conn.cursor() as curs:

        cards_dict = {}

        avito_tyre_brands = get_avito_tyre_brands(\
            url_dict["url_avito_tyres_brands"])
        if avito_tyre_brands == 0:
            send_message('ERROR\n avito_tyre_brands is empty')
            logging.error('<get_cards_from_db> avito_tyre_brands is empty')
            return 0
        
        
        # rims alloy + forged
        # id alloy rims from 1C
        curs.execute(\
        "SELECT * FROM app_product WHERE LOWER(name) LIKE LOWER('%диск%') AND show=true AND 173 = any(imported_from)")
        products_1C = curs.fetchall()
        rims_id_list_1C = []
        for prod in products_1C:
            id = prod[0]
            rims_id_list_1C.append(id)
        cards_dict["rims_id_list_1C"] = rims_id_list_1C
        logging.info('<get_cards_from_db> rims_id_list_1C: ok')
        # all id rims
        curs.execute("SELECT * FROM app_product WHERE LOWER(name) LIKE LOWER('%диск%') AND show=true")
        products = curs.fetchall()
        rims_id_list = []
        for prod in products:
            id = prod[0]
            rims_id_list.append(id)
        logging.info('<get_cards_from_db> rims_id_list: ok')

        rims_image_dict = get_image_dict(sitemap_url=url_dict["url_rims_sitemap"])
        rims_feed_cards = get_rims_feed_cards(url=url_dict["rims_url"], url_moscow=url_dict["rims_moscow_url"], root_url=url_dict["root_url"],\
                            headers=url_dict["headers"])
        logging.info(f'<get_cards_from_db> rims_feed_cards: {len(rims_feed_cards)}')
        
        rims_id_list = list(map(str, rims_id_list))
        curs.execute(f"SELECT * FROM app_rim WHERE product_ptr_id IN ({','.join(rims_id_list)})")
        rim_rows = curs.fetchall()
        if rims_image_dict != 0:
            alloy_cards = parse_rim('alloy', products=products, rim_rows=rim_rows,\
                            image_dict=rims_image_dict, feed_cards=rims_feed_cards)
            if alloy_cards != 0:
                cards_dict['alloy'] = alloy_cards
            logging.info('<get_cards_from_db> alloy_cards: ok')
        
            forged_cards = parse_rim('forged', products=products, rim_rows=rim_rows,\
                            image_dict=rims_image_dict, feed_cards=rims_feed_cards)
            if forged_cards != 0:
                cards_dict['forged'] = forged_cards
            logging.info('<get_cards_from_db> forged_cards: ok')

        del rims_image_dict
        del rims_feed_cards
        del products
        del products_1C
        del rim_rows
        del rims_id_list

        # Deprecated
        # tyres
        # input_tire_strings_list = get_input_tire_strings(input_file_path=input_file_path,\
        #                             input_filename=input_filename)
        # curs.execute("SELECT * FROM app_brand")
        # app_brand = curs.fetchall()
        # brands_dict = {}
        # brands_id_list = []
        # for brand in app_brand:
        #     if brand[1].lower() in TYRE_BRANDS:
        #         brands_dict[brand[0]] = brand[1]
        #         brands_id_list.append(str(brand[0]))
        # del app_brand
        # logging.info(f'<get_cards_from_db> brands_dict: ok , len brands_dict: {len(brands_dict)}')

        # curs.execute(f"SELECT * FROM app_product WHERE LOWER(name) LIKE LOWER('%шин%') AND show=true AND brand_id IN ({','.join(brands_id_list)})")
        # products = curs.fetchall()
        # del brands_id_list
        # tire_id_list = []
        # for prod in products:
        #     id = prod[0]
        #     tire_id_list.append(id)
        # logging.info(f'<get_cards_from_db> len tire_id_list: {len(tire_id_list)}')
        # tire_id_list = list(map(str, tire_id_list))
        # curs.execute(f"SELECT * FROM app_tire WHERE product_ptr_id IN ({','.join(tire_id_list)}) AND diameter IN ({','.join(TYRE_DIAMETRES)})")
        # tire_rows = curs.fetchall()
        # del tire_id_list
        # logging.info(f"<get_cards_from_db> len(tire_rows): {len(tire_rows)}")
        # tire_cards = parse_tire(products=products, tire_rows=tire_rows, brands=brands_dict,\
        #                         brands_avito=avito_tyre_brands, input_tire_strings=input_tire_strings_list)
        # del products
        # del tire_rows
        
        # if tire_cards != 0:
        #     tires_list = get_tires_list(db_list=tire_cards)
        #     if len(tires_list) > 0:
        #         cards_dict['tires'] = tires_list
        #         logging.info(f"<get_cards_from_db> len(tires_list): {len(tires_list)}")
        #     else:
        #         logging.error(f"<get_cards_from_db> tires_list is empty")
        
        # del tire_cards
        # Deprecated
        # springs
        # curs.execute("SELECT * FROM app_product WHERE typeof_id=7 AND show=true")
        # products = curs.fetchall()
        # spring_cards = parse_spring(products=products)
        # if spring_cards != 0:
        #     cards_dict['springs'] = spring_cards

        
        if 'alloy' in cards_dict and 'forged' in cards_dict :
            return cards_dict
        else:
            logging.error('<get_cards_from_db> Cards dict not received')
            logging.error(f"<get_cards_from_db> {cards_dict.keys()}")
            send_message(f"ERROR\nCards dict not received")
            return 0
        

        
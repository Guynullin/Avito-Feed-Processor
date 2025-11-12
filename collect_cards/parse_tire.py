import logging

from difflib import SequenceMatcher
from config import TYRE_BRANDS, TYRE_DIAMETRES

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
            db_brand = 'NOKIAN TYRES'
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
            

    return {'brand': card_brand, 'model' : card_model}

def parse_tire(products: list, tire_rows: list, brands: dict, brands_avito: dict,\
                input_tire_strings: list):
    """returns a list of the tire cards.

    :param products: a list with data from the app_products table.
    :param tire_rows: a list with data from the app_tire table.
    :param brands: a list with data from the app_brands table.
    :param brands_avito: a list containing brands supported by avito.
    :param input_tire_strings: a list with tire titles.
    :return: a list of the tire cards or zero when error occured.
    """
    try:
        default_url = 'https://default.ru/'
        cards = []
        for tire in tire_rows:
            card = {'id': tire[0]}
            card['season'] = tire[1]
            card['spikes'] = tire[2]
            card['load_index'] = tire[3]
            if tire[4] == '-':
                card['speed_index'] = 'U'
            else:
                card['speed_index'] = tire[4]
            card['diameter'] = tire[5]
            card['height'] = tire[6]
            card['width'] = tire[7]
            card['seasonality'] = tire[8]
            
            tire_type = card['seasonality'].replace('Летняя', 'Летние').replace('Зимняя', 'Зимние')\
                .replace('Всесезонная', 'Всесезонные')
            if card['spikes']:
                tire_type = f"{tire_type} шипованные"
            elif tire_type == 'Зимние':
                tire_type = f"{tire_type} нешипованные"
            card['tire_type'] = tire_type
            card['suv'] = tire[9]
            if tire[10] == 0:
                card['runflat'] = 'Нет'
            else:
                card['runflat'] = 'Да'

            flag = 0
            for prod in products:
                if prod[0] == tire[0]:
                    card['title'] = prod[2].replace('*', '-')
                    card['slug'] = prod[3]
                    img_list = []
                    main_pic = prod[5]
                    if isinstance(main_pic, str) and len(main_pic) > 0:
                        if not 'http' in main_pic:
                            img_list.append(default_url + main_pic)
                        else:
                            img_list.append(main_pic)
                    data = prod[16]
                    if isinstance(data, dict) and "replace_pics" in data and isinstance(data["replace_pics"], list):
                        img_links = []
                        replace_pics = data["replace_pics"]
                        for item in replace_pics:
                            if not "http" in item:
                                img_links.append(default_url + item)
                            else:
                                img_links.append(item)
                        if len(img_links) > 0:
                            img_list += img_links
                    if len(img_list) > 0:
                        card['main_img'] = '|'.join(img_list[:10])
                    else:
                        card['main_img'] = None
                    if prod[21] != None and prod[21] > prod[6]:
                        card['price'] = int(prod[21])
                    elif prod[6] != None:
                        card['price'] = int(prod[6])
                    else:
                        card['price'] = None
                        flag = 1
                        break
                    if card['price'] == 0:
                        flag = 1
                        break
                    if prod[9] in brands:
                        brand_model = select_brand_model(brands[prod[9]], prod[10], brands_avito)
                    else:
                        flag = 1
                        break
                    card['brand'] = brand_model['brand']
                    card['model'] = brand_model['model']

                    title = prod[2].replace('Шина', f"{card['seasonality']} шина")\
                        .replace('(Нижнекамский шинный завод) ', '')
                    
                    brand = card['brand'].replace('(Нижнекамский шинный завод)', '')
                    
                    if len(title) > 50:
                        title = f"{card['seasonality']} шина {brand} {card['model']} R{card['diameter']} {card['height']} {card['width']}"
                        if len(title) > 50:
                            title = f"{card['seasonality']} шина {brand} R{card['diameter']} {card['height']} {card['width']}"
                    card['title'] = title.replace('*', '-')

            if flag == 1:
                continue

            if card['price'] == None or flag == 1:
                continue
            if card['model'] == 'Nomodel' or card['brand'] == 'Nobrand':
                continue
            for item in input_tire_strings:
                if str(card['width']).strip() == item["width"].strip()\
                        and str(card['height']).strip() == item["height"].strip()\
                        and str(card['diameter']).strip() in TYRE_DIAMETRES\
                        and card["brand"].lower() in TYRE_BRANDS\
                        and (str(card["season"]).strip().lower() == "зимняя" or\
                            str(card["season"]).strip().lower() == "зима" or\
                            str(card["season"]).strip().lower() == "зимние") :
                    cards.append(card)
                    break

        if len(cards) > 0:
            logging.info(f"<parse_tire> cards: {len(cards)}")
            return cards
        else:
            logging.error(f"<parse_tire> cards is empty, return 0")
            return 0
    
    except Exception as e:
        logging.error(f"<parse_tire> exception: {e}")
        return 0
import logging

from .set_price_and_photo import set_price_and_photo

def try_parse_int(val):
    try:
        int_val = int(val)
        return int_val
    except Exception:
        return 0

def check_dia(in_dia):
    if in_dia == 51.7:
        dia = 52
    elif in_dia == 130.8:
        dia = 131
    elif in_dia == 66.3:
        dia = 66.2
    elif in_dia == 124.3:
        dia = 125
    elif in_dia == 69.6:
        dia = 70
    else:
        dia = in_dia
    return dia

def check_bolts(in_bolts):
    if in_bolts == 135:
        bolts = 8
    else:
        bolts = in_bolts
    return bolts

def check_width(in_width):
    if in_width == 8.75:
        width = 8.5
    else:
        width = in_width
    return width

def check_pcd(in_pcd):
    if in_pcd == 113:
        pcd = 112
    elif in_pcd == 114.312:
        pcd = 114.3 
    else:
        pcd = in_pcd
    return pcd

def parse_rim(rim_type: str, products: list, rim_rows: list, image_dict: dict, feed_cards: list):
    """returns a list of the rims cards by their type.

    :param rim_type: a string with the rims type (alloy|forged|flow_forming).
    :param products: a list with data from the app_products table.
    :param rim_rows: a list with data from the app_rim table.
    :param image_dict: dictionary containing a products slug and 
        a corresponding list of links to images.
    :param feed_cards: a list with product cards from feed.
    :return: a list of the rims cards or zero when error occured.
    """
    cards = []
    cards_id_list = []
    default_url = 'https://default.ru/'
    for rim in rim_rows:
        if rim[11] == rim_type or rim_type == 'alloy' and rim[11] == 'flow_forming':
            card = {'id': rim[0]}
            card['diameter'] = rim[1]
            card['bolts'] = check_bolts(rim[4])
            if rim[5] != 0:
                card['bolts2'] = rim[5]
            card['pcd'] = check_pcd(rim[7])
            if rim[8] != 0:
                card['pcd2'] = rim[8]
            card['width'] = check_width(rim[3])
            card['et'] = rim[2]
            card['dia'] = check_dia(rim[6])
            card['color'] = rim[14]
            card['type'] = rim_type
            card['et2'] = rim[12]
            card['width2'] = rim[13]
            card['rim_brand'] = 'Default'
            for prod in products:
                if prod[0] == rim[0]:
                    card['title'] = prod[2].replace('В СТИЛЕ', 'в стиле').replace('В стиле', 'в стиле')
                    card['slug'] = prod[3]
                    card['in_stock'] = prod[29]
                    if rim_type == 'alloy':
                        data = prod[16]
                        if isinstance(data, dict):
                            if 'efficiency' in data:
                                card['eff'] = try_parse_int(data['efficiency'])
                            elif 'ef_cities' in data:
                                if isinstance(data['ef_cities'], dict) and len(data['ef_cities']) > 0:
                                    card['eff'] = try_parse_int(data['ef_cities'][list(data['ef_cities'].keys())[0]])
                            if 'city_rest_count' in data and isinstance(data['city_rest_count'], dict):
                                city_rest_count = data['city_rest_count']
                                if 'kzn_dorozh' in city_rest_count:
                                    dorozh = try_parse_int(city_rest_count['kzn_dorozh'])
                                    if dorozh > 0:
                                        card['dorozh'] = dorozh
                    elif rim_type == 'forged':
                        data = prod[16]
                        if isinstance(data, dict):
                            if 'own_product' in data and str(data['own_product']) == '1':
                                card['own_product'] = True
                            else:
                                card['own_product'] = False
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
                    
                    card['brand_id'] = prod[9]
                    card['model'] = prod[10]
                    set_price_and_photo(card=card,\
                            image_dict=image_dict, feed_cards=feed_cards, type=rim_type,\
                            rim_diameter=card['diameter'])
                    
            if not "price" in card or card['price'] is None or card['price'] == 0 or\
                not "photo" in card or card["photo"] is None:
                logging.warning(f"<parse_rim> skip card: {card}")
                continue
            if not card["id"] in cards_id_list:
                cards_id_list.append(card["id"])
            else:
                continue
            cards.append(card)
    if len(cards) > 0:
        return cards
    else:
        return 0
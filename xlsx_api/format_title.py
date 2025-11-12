import re
from config import TITLE_FIX_LIST

COLORS = {
    'B': 'Черный',
    'HS': 'Серебирстый',
    'MB': 'Matte black',
    'HB': 'Hyper black',
    'W': 'Белый',
    'MS': 'Matte silver',
    'BM': 'Черный с полировкой',
    'BR': 'Бронза',
    'BML': 'Черный с полированной полкой',
    'MG': 'Графит'
}

def transpose(text: str):
    text_list = text.split(' ')
    index = False
    for item in text_list:
        if re.search(r'[rR]\d\d', str(item)):
            index = text_list.index(item)
            text_list[index].capitalize()
    if index:
        lst1 = text_list[0:index]
        lst2 = text_list[index:]
        lst3 = lst2 + lst1
        new_text = ' '.join(lst3)
        return new_text
    else:
        return text

def format_alloy_title(card: dict, sv: bool=False):
    """returns a formatted string with the alloy rim title.

    :param card: a rim card.
    :param sv: is the product in the 1С database.
    :return: a string.
    """
    # first title


    feed_brand = card["brand"] if "brand" in card else ""
    feed_color = card["color"] if "color" in card else ""

    brand = "Литые диски"
    if "в стиле" in feed_brand.lower():
        brand = f"ДИСКИ {feed_brand.replace('в стиле ', '').replace('В стиле ', '').replace('В СТИЛЕ ', '')}"
    else:
        brand += f" {feed_brand}"
    
    color = ""
    if feed_color in COLORS:
        color = COLORS[feed_color]
    # elif card["color"] in color_dict:
    #     color = color_dict[card["color"]]
    
    diameter = ""
    if "diameter" in card:
        diameter += f"R{card['diameter']}"

    pcd = ""
    if "bolts" in card and "pcd" in card:
        pcd += f"{card['bolts']}x{card['pcd']}"
        if "pcd_2" in card and card['pcd_2'] != 0 and\
            card['pcd_2'] != '0' and card['pcd_2'] != '0.0':
            if "bolts_2" in card  and card['bolts_2'] != 0 and\
            card['bolts_2'] != '0' and card['bolts_2'] != '0.0':
                pcd += f"/{card['bolts_2']}x{card['pcd_2']}"
            else:
                pcd += f"/{card['bolts']}x{card['pcd_2']}"

    
    first_title = f"{brand} {diameter} {pcd}. {color}"

    # description title
    et = card['et']
    if 'et2' in card and card['et2'] != 0:
        et = f'{et}/{card["et2"]}'

    clear_title_J_et = card['feed_title'].replace('ЛИТОЙ ДИСК', 'Литые диски')\
    .replace(card['model'], '').replace(f"({card['color']})", '')\
    .replace(str(card['dia']), '')\
    .replace('dia', '').replace('DIA', '').strip()
    if not 'width2' in card or card['width2'] == 0:
        if card['width'].is_integer():
            clear_string_et = re.sub(rf'\s{int(card["width"])}\w\b', '', clear_title_J_et)                
        else:
            clear_string_et = re.sub(rf'\s{card["width"]}\w\b', '', clear_title_J_et)
    else:
        if card['width'].is_integer():
            width1 = int(card['width'])
        else:
            width1 = card['width']
        if card['width2'].is_integer():
            width2 = int(card['width2'])
        else:
            width2 = card['width2']
        width = f'{width1}/{width2}'
        clear_string_et = re.sub(rf'\s{width}\w\b', '', clear_title_J_et)
    
    clear_string = re.sub(rf"\bET{et}\b", "", clear_string_et).replace(f'ET{card["et"]}', '')
    title = re.sub(" +", " ", clear_string).replace('*', '-').strip()
    
    if color:
        title += f". {color}"

    if sv:
        title = title + ' sv'
    if 'eff' in card:
        if card['eff'] < 27:
            title += ' srt'
        elif card['eff'] >= 27 and card['eff'] <= 35:
            title += ' ave'
        elif card['eff'] > 35:
            title += ' hgh'


    return {"first_title" : first_title, "desc_title" : title}



def format_forged_title(card: dict):
    """returns a formatted string with the forged rim title.

    :param card: a rim card.
    :return: a string.
    """
    # first title
    color_dict = {
        'B': 'Черный',
        'HS': 'Серебирстый',
        'MB': 'Matte black',
        'HB': 'Hyper black',
        'W': 'Белый',
        'MS': 'Matte silver',
        'BM': 'Черный с полировкой',
        'BR': 'Бронза',
        'BML': 'Черный с полированной полкой',
        'MG': 'Графит'
    }

    feed_brand = card["brand"] if "brand" in card else ""
    feed_color = card["color"] if "color" in card else ""

    brand = "Кованые диски"
    if "в стиле" in feed_brand.lower():
        brand = f"ДИСКИ {feed_brand.replace('в стиле ', '').replace('В стиле ', '').replace('В СТИЛЕ ', '')}"
    else:
        brand += f" {feed_brand}"
    color = ""
    if feed_color in color_dict:
        color = color_dict[feed_color]
    # elif card["color"] in color_dict:
    #     color = color_dict[card["color"]]
    
    diameter = ""
    if "diameter" in card:
        diameter += f"R{card['diameter']}"

    pcd = ""
    if "bolts" in card and "pcd" in card:
        pcd += f"{card['bolts']}x{card['pcd']}"
        if "pcd_2" in card and card['pcd_2'] != 0 and\
            card['pcd_2'] != '0' and card['pcd_2'] != '0.0':
            if "bolts_2" in card  and card['bolts_2'] != 0 and\
                card['bolts_2'] != '0' and card['bolts_2'] != '0.0':
                pcd += f"/{card['bolts_2']}x{card['pcd_2']}"
            else:
                pcd += f"/{card['bolts']}x{card['pcd_2']}"

    
    first_title = f"{brand} {diameter} {pcd}. {color}"

    # description title
    et = card['et']
    if 'et2' in card and card['et2'] != 0:
        et = f'{et}/{card["et2"]}'

    clear_title_J_et = card['feed_title'].replace('КОВАНЫЙ ДИСК', 'Кованые диски')\
    .replace(card['model'], '').replace(f"({card['color']})", '')\
    .replace(str(card['dia']), '')\
    .replace('dia', '').replace('DIA', '').strip()
    if not 'width2' in card or card['width2'] == 0:
        if card['width'].is_integer():
            clear_string_et = re.sub(rf'\s{int(card["width"])}\w\b', '', clear_title_J_et)                
        else:
            clear_string_et = re.sub(rf'\s{card["width"]}\w\b', '', clear_title_J_et)
    else:
        if card['width'].is_integer():
            width1 = int(card['width'])
        else:
            width1 = card['width']
        if card['width2'].is_integer():
            width2 = int(card['width2'])
        else:
            width2 = card['width2']
        width = f'{width1}/{width2}'
        clear_string_et = re.sub(rf'\s{width}\w\b', '', clear_title_J_et)
    
    clear_string = re.sub(rf"\bET{et}\b", "", clear_string_et).replace(f'ET{card["et"]}', '')
    title = re.sub(" +", " ", clear_string).replace('*', '-').strip()

    if len(title) > 50:
        title = title.replace('RZ FORGED ', '')
        if len(title) > 50:
            title = title.replace(f"{card['bolts']}x{card['pcd']}", '')\
                .replace(f"{card['bolts']}X{card['pcd']}", '').strip()
    
    if color:
        title += f". {color}"
    
    if card.get('in_stock', False) or card.get('own_product', False):
        title = f'{title}. В наличии'

    return {"first_title" : first_title, "desc_title" : title}

def format_title_by_city_new(src_title: str, dor = None):
    """returns a formatted string with the rim title.

    :param title: a source card title.
    :return: a string.
    """
    # 'тип диска+диаметр+сверловка+название диска'
    title = src_title
    
    for item in TITLE_FIX_LIST:
        if item in title:
            title = title.replace(item, '')
    title = title.strip()

    if 'кованый диск' in title.lower():
        pattern = re.compile("кованый диск", re.IGNORECASE)
        text = pattern.sub("", title)
        title = 'Кованые диски ' + transpose(text)
    elif 'кованный диск' in title.lower():
        pattern = re.compile("кованный диск", re.IGNORECASE)
        text = pattern.sub("", title)
        title = 'Кованые диски ' + transpose(text)
    elif 'кованые диски' in title.lower():
        pattern = re.compile("кованые диски", re.IGNORECASE)
        text = pattern.sub("", title)
        title = 'Кованые диски ' + transpose(text)
    elif 'кованные диски' in title.lower():
        pattern = re.compile("кованные диски", re.IGNORECASE)
        text = pattern.sub("", title)
        title = 'Кованые диски ' + transpose(text)
    elif 'литые диски' in title.lower():
        pattern = re.compile("литые диски", re.IGNORECASE)
        text = pattern.sub("", title)
        title = 'Литые диски ' + transpose(text)
    elif 'литой диск' in title.lower():
        pattern = re.compile("литой диск", re.IGNORECASE)
        text = pattern.sub("", title)
        title = 'Литые диски ' + transpose(text)

    clear_title =  re.sub(r'\shgh\b|\ssrt\b|\save\b', '', title)

    if dor and dor != 0:
        return f"{clear_title.replace('  ', ' ').strip()} dor"
    else:
        return clear_title.replace('  ', ' ').strip()
    
def generate_rims_title(card):

    pattern = re.compile(re.escape('в стиле'), re.IGNORECASE)
    brand = pattern.sub("", card["brand"])

    color = ""
    if "color" in card and card["color"] in COLORS:
        color = COLORS[card["color"]]
    
    width = ""
    if 'width2' in card and 'width' in card:
        width = f" {card['width']}/{card['width2']}J"
    elif 'width' in card:
        width = f" {card['width']}J"
    
    pcd = ""
    if "pcd2" in card and "bolts2" in card and "pcd" in card and "bolts" in card:
        pcd = f" {card['bolts']}x{card['pcd']}/{card['bolts2']}x{card['pcd2']}"
    elif "pcd2" in card and "pcd" in card and "bolts" in card:
        pcd = f" {card['bolts']}x{card['pcd']}/{card['bolts']}x{card['pcd2']}"
    elif "bolts2" in card and "pcd" in card and "bolts" in card:
        pcd = f" {card['bolts']}x{card['pcd']}/{card['bolts2']}x{card['pcd']}"
    elif "pcd" in card and "bolts" in card:
        pcd = f" {card['bolts']}x{card['pcd']}"

    et = ""
    if 'et2' in card and 'et' in card:
        et = f" et{card['et']}/{card['et2']}"
    elif 'et' in card:
        width = f" et{card['et']}"
    
    dia = ""
    if 'dia2' in card and 'dia' in card:
        dia = f" dia{card['dia']}/{card['dia2']}"
    elif 'dia' in card:
        dia = f" dia{card['dia']}"

    if card['type'] == 'forged':
        title_template = f"Кованые диски {brand} {card['model']} R{card['diameter']}{width}{pcd}{et}{dia} {color}"
    elif card['type'] == 'alloy' or card['type'] == 'flow_forming':
        title_template = f"Литые диски {brand} {card['model']} R{card['diameter']}{width}{pcd}{et}{dia} {color}"
    else:
        return None  
    

    if len(title_template) <= 50:
        return title_template

    title_template = title_template.replace(dia, "")
    if len(title_template) <= 50:
        return title_template
    
    title_template = title_template.replace(f" {brand}", "")
    if len(title_template) <= 50:
        return title_template

    title_template = title_template.replace(et, "")
    if len(title_template) <= 50:
        return title_template


    return title_template[:50]


def generate_tyres_title(card):
    db_brand = card['brand']
    
    if 'NOKIAN TYRES'.lower() in db_brand.lower():
        db_brand = 'Ikon Tyres'
        print(f"nokian: {card}")
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

    title_template = f"{card['seasonality']} шина {db_brand} {card['model']} {card['width']} R{card['diameter']} {card['load_index']}{card['speed_index']}"


    if len(title_template) <= 50:
        return title_template
    else:
        new_title_template = f"{card['seasonality']} шина {db_brand} {card['width']} R{card['diameter']} {card['load_index']}{card['speed_index']}"
        if len(new_title_template) <= 50:
            return new_title_template
        
    return title_template[:50]
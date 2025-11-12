import os
import copy
import random 
import logging
import xml.etree.ElementTree as ET

from datetime import datetime, timedelta
from typing import Dict, Any, List
from .get_prices import get_alloy_price, get_moscow_alloy_price
from xlsx_api import format_forged_rim_desc_by_city, format_alloy_rim_desc_by_city,\
    format_tire_desc_by_city, format_alloy_rim_desc_by_city_msk_piter_new,\
    format_forged_rim_desc_by_city_msk_piter_new, format_tire_desc_by_city_msk_piter_new,\
    format_alloy_rim_desc_by_city_and_diameter, format_title_by_city_new, format_tire_desc,\
    format_alloy_rim_desc_tumen
from config import CITY_DATA, WEB_PATH, RIM_DIAMETER_LIST, FORGED_VIDEO_FILE_URL

delivery_desc = '''

Как заказать через Авито.Доставку?
Простые шаги для заказа:
1. Найдите комплект дисков на Авито.
2. Проверьте характеристики и наличие.
3. Выберите «Купить с доставкой» и ТК ПЭК.
4. Укажите данные и оплатите (безопасная сделка).
5. Получите диски в ПВЗ за 3–7 дня и проверьте заказ.
'''

# delivery_cities = {'avito_kzn.xml', 'avito_msk.xml', 
#                    'avito_krasnodar.xml', 'avito_krasnoyarsk.xml', 
#                    'avito_smr.xml', 'avito_ufa.xml', 'avito_rostovnd.xml',
#                    'avito_other_ekb.xml', 'avito_other_tmn.xml'}

moscow_city_list = [
    'avito_msk.xml',
    'avito_msk_portfolio.xml',
    'avito_msk_stocks.xml',
]

no_portfolio_cities = {'avito_piter_new.xml', 'avito_msk_new.xml'}

no_tires_cities = {'avito_piter_new.xml',
                    'avito_msk_new.xml', 
                    'avito_other_ekb.xml', 
                    'avito_other_tmn.xml'}

other_cities = {'avito_other_ekb.xml', 
                'avito_other_tmn.xml'}

simple_id_cities = {'avito_msk_new.xml', 
                    'avito_volgograd.xml',
                    'avito_volgograd_dorozh.xml',
                    'avito_chel.xml',
                    'avito_chel_dorozh.xml',
                    'avito_krasnoyarsk.xml',
                    'avito_krasnoyarsk_dorozh.xml',
                    'avito_smr.xml',
                    'avito_smr_stocks.xml',
                    'avito_smr_dorozh.xml', 
                    'avito_khmao.xml',
                    'avito_khmao_dorozh.xml'}

dorozh_stock_cities = {'avito_perm_dorozh.xml', 'avito_volgograd_dorozh.xml',
                        'avito_krasnoyarsk_dorozh.xml', 'avito_rostovnd_dorozh.xml',
                        'avito_omsk_dorozh.xml', 'avito_novosib_dorozh.xml',
                        'avito_chel_dorozh.xml', 'avito_piter_dorozh.xml',
                        'avito_ufa_dorozh.xml', 'avito_voron_dorozh.xml',
                        'avito_krasnodar_dorozh.xml', 'avito_kzn_dorozh.xml',
                        'avito_msk_dorozh.xml', 'avito_smr_dorozh.xml',
                        'avito_n_nov_dorozh.xml', 'avito_other_ekb.xml',
                        'avito_other_tmn.xml', 'avito_khmao_dorozh.xml'}

portfolio_cities = {'avito_khmao_portfolio.xml', 'avito_perm_portfolio.xml',
                    'avito_volgograd_portfolio.xml', 'avito_krasnoyarsk_portfolio.xml',
                    'avito_rostovnd_portfolio.xml', 'avito_omsk_portfolio.xml',
                    'avito_novosib_portfolio.xml', 'avito_chel_portfolio.xml',
                    'avito_piter_portfolio.xml', 'avito_ufa_portfolio.xml',
                    'avito_voron_portfolio.xml', 'avito_krasnodar_portfolio.xml',
                    'avito_kzn_portfolio.xml', 'avito_msk_portfolio.xml',
                    'avito_n_nov_portfolio.xml'}

new_id_list = [733138, 725771, 725758, 725770, 725775, 725744, 
               725777, 725752, 725776, 725779, 725749, 725768, 725751, 725781]

def try_parse_int(val):
    try:
        int_val = int(val)
        return int_val
    except Exception:
        return None

def generate_avito_stock_xml(output_path: str, cards: List[Dict[str, Any]]) -> None:
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    
    cities = {
        'dorozh': {
            'stock_key': ['rest_count_kzn_dorozh'],
            'filename': 'avito_dorozh_stocks_rz_list.xml'
        },
        'kazan': {
            'stock_key': ['rest_count_kazan', 'rest_count_kzn_dorozh'],
            'filename': 'avito_kazan_stocks_rz_list.xml'
        },
        'msk': {
            'stock_key': ['rest_count_msk', 'rest_count_kzn_dorozh'],
            'filename': 'avito_msk_stocks_rz_list.xml'
        },
    }
    
    for city, params in cities.items():
        record_path = os.path.join(output_path, params['filename'])
        stock_keys = params['stock_key']
        
        with open(record_path, 'w', encoding='utf-8') as xml:
            xml.write(f'<items date="{date}" formatVersion="1">\n')
            
            items_data = {}
            
            for card in cards:
                if 'Id' not in card:
                    continue
                    
                if 'DateEnd' in card and card['DateEnd'] is not None:
                    continue
                
                card_id = card['Id']
                total_stock = 0
                
                for stock_key in stock_keys:
                    if stock_key in card:
                        stock_value = card[stock_key]
                        if isinstance(stock_value, int) and stock_value > 0:
                            total_stock += stock_value
                
                if total_stock > 0:
                    items_data[card_id] = total_stock
            
            for card_id, stock in items_data.items():
                xml.write('<item>\n')
                if int(card_id) in new_id_list:
                    xml.write(f'<id>NZ{card_id}373</id>\n')
                else:
                    xml.write(f'<id>RZ{card_id}373</id>\n')
                xml.write(f'<stock>{stock}</stock>\n')
                xml.write('</item>\n')
                
            xml.write('</items>')
    

def simple_id_generate_avito_stock_xml(output_path: str, cards: List[Dict[str, Any]]) -> None:
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    
    cities = {
        'dorozh': {
            'stock_key': ['rest_count_kzn_dorozh'],
            'filename': 'avito_dorozh_stocks_simple_id_list.xml'
        },
        'samara': {
            'stock_key': ['rest_count_samara', 'rest_count_kzn_dorozh'],
            'filename': 'avito_samara_stocks_simple_id_list.xml'
        },
    }
    
    for city, params in cities.items():
        record_path = os.path.join(output_path, params['filename'])
        stock_keys = params['stock_key']
        
        with open(record_path, 'w', encoding='utf-8') as xml:
            xml.write(f'<items date="{date}" formatVersion="1">\n')
            
            items_data = {}
            
            for card in cards:
                if 'Id' not in card:
                    continue
                    
                if 'DateEnd' in card and card['DateEnd'] is not None:
                    continue
                
                card_id = card['Id']
                total_stock = 0
                
                for stock_key in stock_keys:
                    if stock_key in card:
                        stock_value = card[stock_key]
                        if isinstance(stock_value, int) and stock_value > 0:
                            total_stock += stock_value
                
                if total_stock > 0:
                    items_data[card_id] = total_stock
            
            for card_id, stock in items_data.items():
                xml.write('<item>\n')
                xml.write(f'<id>{card_id}</id>\n')
                xml.write(f'<stock>{stock}</stock>\n')
                xml.write('</item>\n')
                
            xml.write('</items>')

def record_xml(cards:dict):
    """Writes data from the dictionary with product cards to a xml file.

    :param cards: a product cards.
    :return: 1 if the recording is successful. 
    """
    for city in CITY_DATA:
        cards_dict = copy.deepcopy(cards)
        web_path = os.path.join(WEB_PATH, city)
        contacts = CITY_DATA[city]

        with open(web_path, 'w', encoding='utf-8') as xml:
            xml.write('<Ads formatVersion="3" target="Avito.ru">\n')
            for card_list in cards_dict:
                if card_list == 'alloy_rims_cards' or card_list == 'forged_rims_cards':
                    if card_list == 'alloy_rims_cards':
                        cards_for_stocks_file = cards_dict['alloy_rims_cards'] + cards_dict['forged_rims_cards']
                        generate_avito_stock_xml(output_path=WEB_PATH, cards=cards_for_stocks_file)
                        simple_id_generate_avito_stock_xml(output_path=WEB_PATH, cards=cards_for_stocks_file)
                    for card in cards_dict[card_list]:
                        if "VideoFileURL" in card and card["VideoFileURL"]:
                            video_file_url = card["VideoFileURL"]
                        else:
                            video_file_url = None
                        quantity = 'за 1 шт.'
                        delivery = []
                        franchisees = False
                        portfolio = False
                        stock = None
                        desc = card["Description"]
                        title = card['Title'].replace('Литой диск', 'Литые диски').replace('Кованый диск', 'Кованые диски')
                        price = int(card["Price"])
                        if card_list == 'alloy_rims_cards' or card_list == 'forged_rims_cards':
                            if city in portfolio_cities:
                                if 'portfolio' in card and card['portfolio'] == True:
                                    portfolio = True
                                else:
                                    continue
                            elif 'portfolio' in card and card['portfolio'] == True and city not in portfolio_cities:
                                continue
                            
                            if city == 'avito_msk.xml':
                                new_price = get_moscow_alloy_price(card, 'promo_price_msk')
                                if new_price:
                                    price = new_price['price']
                            else:
                                new_price = get_alloy_price(card, 'promo_price')
                                if new_price:
                                    price = new_price
                        
                        if city == 'avito_piter_new.xml':
                            card['Id'] = f"A{card['Id']}"
                        elif city in simple_id_cities:
                            if card_list == 'forged_rims_cards':
                                video_file_url = FORGED_VIDEO_FILE_URL
                        else:
                            if card_list == 'forged_rims_cards':
                                video_file_url = FORGED_VIDEO_FILE_URL
                            if int(card['Id']) in new_id_list:
                                card['Id'] = f"NZ{card['Id']}373"
                            else:
                                card['Id'] = f"RZ{card['Id']}373"


                        # Delivery
                        if city in moscow_city_list:
                            if card_list == 'alloy_rims_cards' or card_list == 'forged_rims_cards':
                                delivery = ['ПВЗ']

                        # dorozh franchisees
                        if city in dorozh_stock_cities:
                            if 'rest_count_kzn_dorozh' in card and isinstance(card['rest_count_kzn_dorozh'], int) and card['rest_count_kzn_dorozh'] > 0:
                                if card_list == 'alloy_rims_cards' or card_list == 'forged_rims_cards':
                                    if city != 'avito_msk_dorozh.xml':
                                        delivery = ['Свой партнёр ПЭК', 'ПВЗ']
                                    else:
                                        delivery = ['ПВЗ']
                                    stock = card['rest_count_kzn_dorozh']
                                    franchisees = True
                                    if stock %4 == 0:
                                        quantity = 'за 4 шт.'
                                        price *= 4 
                                        desc = desc.replace('Цена указанa за oдин диск. ', 'Цена указанa за комплект дисков 4шт. ')
                                        desc = desc + delivery_desc
                                        desc = 'Абсолютно новые диски в НАЛИЧИИ! Упакованы в четыре коробки и готовы к установке на ваш автомобиль\n' + desc
                                        desc = desc + '\ndl\n'
                                        if len(title) <= 47:
                                            title += ' dl'
                                        else:
                                            title = title[:47] + ' dl'
                            else:
                                continue
                        elif 'rest_count_kzn_dorozh' in card and isinstance(card['rest_count_kzn_dorozh'], int) and card['rest_count_kzn_dorozh'] > 0:
                            continue

                        # kazan offline
                        if city == 'avito_kzn_stocks.xml':
                            if 'rest_count_kazan' in card and isinstance(card['rest_count_kazan'], int) and card['rest_count_kazan'] > 0:
                                if card_list == 'alloy_rims_cards' or card_list == 'forged_rims_cards':
                                    delivery = []
                                    stock = card['rest_count_kazan']
                                    
                                    if stock %4 == 0:
                                        quantity = 'за 4 шт.'
                                        price *= 4 
                                        desc = desc.replace('Цена указанa за oдин диск. ', 'Цена указанa за комплект дисков 4шт. ')
                                        desc = desc + delivery_desc
                                        desc = desc + '\nkw\n'
                                        if len(title) <= 47:
                                            title += ' kw'
                                        else:
                                            title = title[:47] + ' kw'
                            else:
                                continue
                        elif 'rest_count_kazan' in card and isinstance(card['rest_count_kazan'], int) and card['rest_count_kazan'] > 0:
                            continue

                        # moscow offline
                        if city == 'avito_msk_stocks.xml':
                            if 'rest_count_msk' in card and isinstance(card['rest_count_msk'], int) and card['rest_count_msk'] > 0:
                                if card_list == 'alloy_rims_cards' or card_list == 'forged_rims_cards':
                                    delivery = []
                                    stock = card['rest_count_msk']
                                    
                                    if stock %4 == 0:
                                        quantity = 'за 4 шт.'
                                        price *= 4 
                                        desc = desc.replace('Цена указанa за oдин диск. ', 'Цена указанa за комплект дисков 4шт. ')
                                        desc = desc + delivery_desc
                                        desc = desc + '\nmw\n'
                                        if len(title) <= 47:
                                            title += ' mw'
                                        else:
                                            title = title[:47] + ' mw'
                            else:
                                continue
                        elif 'rest_count_msk' in card and isinstance(card['rest_count_msk'], int) and card['rest_count_msk'] > 0:
                            continue

                        # samara offline
                        if city == 'avito_smr_stocks.xml':
                            if 'rest_count_samara' in card and isinstance(card['rest_count_samara'], int) and card['rest_count_samara'] > 0:
                                if card_list == 'alloy_rims_cards' or card_list == 'forged_rims_cards':
                                    delivery = []
                                    stock = card['rest_count_samara']
                                    
                                    if stock %4 == 0:
                                        quantity = 'за 4 шт.'
                                        price *= 4 
                                        desc = desc.replace('Цена указанa за oдин диск. ', 'Цена указанa за комплект дисков 4шт. ')
                                        desc = desc + delivery_desc
                                        desc = desc + '\nsw\n'
                                        if len(title) <= 47:
                                            title += ' sw'
                                        else:
                                            title = title[:47] + ' sw'
                            else:
                                continue
                        elif 'rest_count_samara' in card and isinstance(card['rest_count_samara'], int) and card['rest_count_samara'] > 0:
                            continue

                        # Offline shops descriptions
                        if city == 'avito_kzn.xml' or city == 'avito_smr.xml'\
                            or city == 'avito_msk.xml':
                            
                            specs = card.get('specs')
                            if card_list == 'alloy_rims_cards':
                                if not card['RimDiameter'] in RIM_DIAMETER_LIST:
                                    desc = format_alloy_rim_desc_by_city(title=card['Title'], 
                                        pcd=f"{card.get('RimBolts', '')}x{float(card.get('RimBoltsDiameter', ''))}%{float(card.get('RimDIA', ''))}${card.get('RimDiameter', '')}",
                                        city=city, specs=specs)
                                else:
                                    desc = format_alloy_rim_desc_by_city_and_diameter(title=card['Title'], 
                                        pcd=f"{card.get('RimBolts', '')}x{float(card.get('RimBoltsDiameter', ''))}%{float(card.get('RimDIA', ''))}${card.get('RimDiameter', '')}",
                                        city=city)
                            elif card_list == 'forged_rims_cards':
                                desc = format_forged_rim_desc_by_city(
                                    title=card['Title'], 
                                    pcd=f"{card.get('RimBolts', '')}x{float(card.get('RimBoltsDiameter', ''))}%{float(card.get('RimDIA', ''))}${card.get('RimDiameter', '')}", 
                                    city=city, 
                                    specs=specs)
                        # Dublicate accounts 
                        elif city == 'avito_piter_new.xml' or city == 'avito_msk_new.xml':
                            if video_file_url:
                                video_file_url = None
                            
                            title = format_title_by_city_new(card['Title'])
                            if card_list == 'alloy_rims_cards':
                                if city == 'avito_msk_new.xml':
                                    new_price = get_moscow_alloy_price(card, 'market_price_msk')
                                    if new_price:
                                        price = new_price['price']
                                        if not new_price['is_origin']:
                                            title += '. В наличии'
                                elif city == 'avito_piter_new.xml':
                                    new_price = get_alloy_price(card, 'market_price')
                                    if new_price:
                                        price = new_price
                                        title += '. В наличии'
                            # card['RimBrand'] = 'RZ Forged'
                            if city == 'avito_piter_new.xml':
                                card['CompanyName'] = 'Магазин стильных колес'
                            else:
                                card['CompanyName'] = 'Wagon Wheels'
                            card['ManagerName'] = 'звонок бесплатный'
                            if isinstance(card['main_img'], str) and len(card['main_img']) > 0:
                                if card['main_img'] == '111|222':
                                    continue
                                card['ImageUrls'] = card['main_img']
                            else:
                                continue
                            if card_list == 'alloy_rims_cards':
                                desc = format_alloy_rim_desc_by_city_msk_piter_new(
                                    title=card['Title'], 
                                    pcd=f"{card.get('RimBolts', '')}x{float(card.get('RimBoltsDiameter', ''))}%{float(card.get('RimDIA', ''))}${card.get('RimDiameter', '')}", 
                                    city=city)
                            elif card_list == 'forged_rims_cards':
                                desc = format_forged_rim_desc_by_city_msk_piter_new(
                                    title=card['Title'], 
                                    pcd=f"{card.get('RimBolts', '')}x{float(card.get('RimBoltsDiameter', ''))}%{float(card.get('RimDIA', ''))}${card.get('RimDiameter', '')}", 
                                    city=city)
                        
                        # Franchisees
                        if city == 'avito_other_ekb.xml' and not franchisees:
                            continue
                        elif city == 'avito_other_ekb.xml' and franchisees:
                            if "RimDiameter" in card and try_parse_int(card["RimDiameter"]):
                                rim_diameter = try_parse_int(card["RimDiameter"])
                                if rim_diameter < 17:
                                    continue
                            else:
                                continue
                        
                        if city == 'avito_other_tmn.xml' and not franchisees:
                            continue
                        elif city == 'avito_other_tmn.xml' and franchisees:
                            desc = format_alloy_rim_desc_tumen(
                                title=card['Title'], 
                                pcd=f"{card.get('RimBolts', '')}x{float(card.get('RimBoltsDiameter', ''))}%{float(card.get('RimDIA', ''))}${card.get('RimDiameter', '')}")
                            if stock %4 == 0:
                                if "RimDiameter" in card and try_parse_int(card["RimDiameter"]):
                                    rim_diameter = try_parse_int(card["RimDiameter"])
                                    if rim_diameter == 15:
                                        price = 42000
                                    elif rim_diameter == 16:
                                        price = 50000
                                    elif rim_diameter == 17:
                                        price = 67000
                                    elif rim_diameter == 18:
                                        price = 76000
                                    elif rim_diameter == 19:
                                        price = 87000
                                    elif rim_diameter == 20:
                                        price = 100000
                                    elif rim_diameter == 21:
                                        price = 110000
                                else:
                                    continue
                            else:
                                continue

                        xml.write('<Ad>\n')

                        xml.write(f'<Id>{card["Id"]}</Id>\n')
                        xml.write(f'<Category>{card["Category"]}</Category>\n')
                        # xml.write(f'<TypeId>{card["TypeId"]}</TypeId>\n')
                        xml.write(f'<AdType>{card["AdType"]}</AdType>\n')
                        # if 'DateBegin_val' in card and card['DateBegin_val']:
                        #     xml.write(f'<DateBegin>{card["DateBegin_val"]}</DateBegin>\n')
                        xml.write(f'<Condition>{card["Condition"]}</Condition>\n')
                        # 
                        xml.write(f'<ProductType>{card["ProductType"]}</ProductType>\n')
                        xml.write(f'<GoodsType>{card["GoodsType"]}</GoodsType>\n')
                        xml.write(f'<AvitoStatus>{card["AvitoStatus"]}</AvitoStatus>\n')
                        if "AdStatus" in card:
                            xml.write(f'<AdStatus>{card["AdStatus"]}</AdStatus>\n')
                        xml.write(f'<ContactMethod>{card["ContactMethod"]}</ContactMethod>\n')
                        xml.write(f'<ListingFee>{card["ListingFee"]}</ListingFee>\n')
                        xml.write(f'<CompanyName>{card["CompanyName"]}</CompanyName>\n')
                        xml.write(f'<EMail>{contacts["email"]}</EMail>\n')
                        if "RimBrand" in card and card["RimBrand"]:
                            if card["RimBrand"] != "False":
                                xml.write(f'<RimBrand>{card["RimBrand"]}</RimBrand>\n')
                            else:
                                card["DateEnd"] = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
                        if "RimModel" in card and card["RimModel"] != "False" and card["RimModel"]:
                            xml.write(f'<RimModel>{card["RimModel"]}</RimModel>\n')
                        xml.write(f'<RimDiameter>{card["RimDiameter"]}</RimDiameter>\n')
                        xml.write(f'<RimDIA>{card["RimDIA"]}</RimDIA>\n')
                        xml.write(f'<RimType>{card["RimType"]}</RimType>\n')
                        xml.write(f'<RimWidth>{card["RimWidth"]}</RimWidth>\n')
                        xml.write(f'<RimBolts>{card["RimBolts"]}</RimBolts>\n')
                        xml.write(f'<RimBoltsDiameter>{card["RimBoltsDiameter"]}</RimBoltsDiameter>\n')
                        xml.write(f'<RimOffset>{card["RimOffset"]}</RimOffset>\n')
                        xml.write(f'<ManagerName>{card["ManagerName"]}</ManagerName>\n')
                        xml.write(f'<ContactPhone>{contacts["phone"]}</ContactPhone>\n')
                        xml.write(f'<Address>{random.choice(contacts["adress"])}</Address>\n')
                        xml.write(f'<Title>{title.replace("&", "&amp;")}</Title>\n')
                        xml.write(f'<Description><![CDATA[{desc.replace("%title%", card["Title"]).replace("&", "&amp;")}]]></Description>\n')
                        xml.write(f'<Price>{price}</Price>\n')
                        if 'DateEnd' in card and card['DateEnd'] is not None:
                            xml.write(f"<DateEnd>{card['DateEnd']}</DateEnd>\n")
                        xml.write(f'<Quantity>{quantity}</Quantity>\n')
                        if delivery and city not in other_cities:
                            xml.write(f'<Delivery>\n')
                            for item in delivery:
                                xml.write(f'<Option>{item}</Option>\n')
                            xml.write(f'</Delivery>')
                        if stock:
                            xml.write(f'<Stock>{stock}</Stock>\n')
                        xml.write(f'<Images>\n')
                        for image in card['ImageUrls'].split('|'):
                            if city == 'avito_other_tmn.xml':
                                if 'акция' in image.lower():
                                    continue
                            xml.write(f'<Image url="{image.strip()}"/>\n')
                        xml.write(f'</Images>\n')
                        if "VideoUrl" in card and card["VideoUrl"]:
                            xml.write(f'<VideoUrl>{card["VideoUrl"]}</VideoUrl>\n')
                        if video_file_url:
                            if not 'CDATA' in video_file_url:
                                xml.write(f'<VideoFileURL><![CDATA[{video_file_url}]]></VideoFileURL>\n')
                            else:
                                xml.write(f'<VideoFileURL>{video_file_url}</VideoFileURL>\n')
                        if portfolio and city in portfolio_cities: 
                            xml.write(f'<portfolio>{portfolio}</portfolio>\n')
                        xml.write('</Ad>\n')
                # Springs
                # elif card_list == 'springs_cards':
                #     if city == 'avito_piter_new.xml' or city == 'avito_msk_new.xml':
                #         continue
                #     else:
                #         for card in cards_dict[card_list]:
                #             xml.write('<Ad>\n')
                #             xml.write(f'<Id>{card["Id"]}</Id>\n')
                #             xml.write(f'<Category>{card["Category"]}</Category>\n')
                #             # xml.write(f'<TypeId>{card["TypeId"]}</TypeId>\n')
                #             xml.write(f'<AdType>{card["AdType"]}</AdType>\n')
                #             xml.write(f'<Condition>{card["Condition"]}</Condition>\n')
                #             # 
                #             xml.write(f'<ProductType>{card["ProductType"]}</ProductType>\n')
                #             xml.write(f'<GoodsType>{card["GoodsType"]}</GoodsType>\n')
                #             xml.write(f'<AvitoStatus>{card["AvitoStatus"]}</AvitoStatus>\n')
                #             if "AdStatus" in card:
                #                 xml.write(f'<AdStatus>{card["AdStatus"]}</AdStatus>\n')
                #             xml.write(f'<ContactMethod>{card["ContactMethod"]}</ContactMethod>\n')
                #             xml.write(f'<ListingFee>{card["ListingFee"]}</ListingFee>\n')
                #             xml.write(f'<CompanyName>{card["CompanyName"]}</CompanyName>\n')
                #             xml.write(f'<EMail>{contacts["email"]}</EMail>\n')
                #             xml.write(f'<Brand>{card["Brand"]}</Brand>\n')
                #             xml.write(f'<Model>{card["Model"]}</Model>\n')
                #             xml.write(f'<Availability>{card["Availability"]}</Availability>\n')
                #             xml.write(f'<SparePartType>{card["SparePartType"]}</SparePartType>\n')
                #             xml.write(f'<Make>{card["Make"]}</Make>\n')
                #             xml.write(f'<Originality>{card["Originality"]}</Originality>\n')
                #             xml.write(f'<OEM>{card["OEM"]}</OEM>\n')
                #             xml.write(f'<Modification>{card["Modification"]}</Modification>\n')
                #             xml.write(f'<BodyType>{card["BodyType"]}</BodyType>\n')
                #             xml.write(f'<Doors>{card["Doors"]}</Doors>\n')
                #             xml.write(f'<Generation>{card["Generation"]}</Generation>\n')
                #             # 
                #             xml.write(f'<ContactPhone>{contacts["phone"]}</ContactPhone>\n')
                #             xml.write(f'<Address>{random.choice(contacts["adress"])}</Address>\n')
                #             xml.write(f'<Title>{card["Title"].replace("&", "&amp;")}</Title>\n')
                #             xml.write(f'<Description><![CDATA[{card["Description"].replace("&", "&amp;")}]]></Description>\n')
                #             xml.write(f'<Price>{card["Price"]}</Price>\n')
                #             xml.write(f'<Images>\n')
                #             for image in card['ImageUrls'].split('|'):
                #                 xml.write(f'<Image url="{image.strip()}"/>\n')
                #             xml.write(f'</Images>\n')
                #             xml.write('</Ad>\n')

                # Tires
                # elif card_list == 'tires_cards' and city not in no_tires_cities:
                #     for card in cards_dict[card_list]:
                #         desc = card["Description"]
                #         if city == 'avito_piter_new.xml':
                #             card['Id'] = f"A{card['Id']}"
                #         elif city == 'avito_msk_new.xml' or city == 'avito_volgograd.xml'\
                #             or city == 'avito_chel.xml' or city == 'avito_krasnoyarsk.xml'\
                #             or city == 'avito_smr.xml' or city == 'avito_khmao.xml':
                #             pass
                #         else:
                #             card['Id'] = f"RZ{card['Id']}373"
                        
                #         if city == 'avito_kzn.xml' or city == 'avito_smr.xml'\
                #             or city == 'avito_msk.xml':
                #             desc = format_tire_desc_by_city(card=card, city=city)
                #         elif city == 'avito_piter_new.xml' or city == 'avito_msk_new.xml':
                #             # if 'DateBegin' in card and card['DateBegin']:
                #             #     card['DateBegin_val'] = card['DateBegin']
                #             # else:
                #             #     continue
                            
                #             desc = format_tire_desc_by_city_msk_piter_new(card=card, city=city, season=card['TireType'])
                #             if isinstance(card['main_img'], str) and len(card['main_img']) > 0:
                #                 if card['main_img'] == '111|222':
                #                     continue
                #                 card['ImageUrls'] = card['main_img']
                #             else:
                #                 continue
                #             if city == 'avito_piter_new.xml':
                #                 card['CompanyName'] = 'Магазин стильных колес'
                #             else:
                #                 card['CompanyName'] = 'Wagon Wheels'
                #         else:
                #             desc = format_tire_desc(card=card)
                #         xml.write('<Ad>\n')
                #         xml.write(f'<Id>{card["Id"]}</Id>\n')
                #         xml.write(f'<Category>{card["Category"]}</Category>\n')
                #         # xml.write(f'<TypeId>{card["TypeId"]}</TypeId>\n')
                #         # if 'DateBegin_val' in card and card['DateBegin_val']:
                #         #     xml.write(f'<DateBegin>{card["DateBegin_val"]}</DateBegin>\n')
                #         xml.write(f'<AdType>{card["AdType"]}</AdType>\n')
                #         xml.write(f'<Condition>{card["Condition"]}</Condition>\n')
                #         # 
                #         xml.write(f'<ProductType>{card["ProductType"]}</ProductType>\n')
                #         xml.write(f'<GoodsType>{card["GoodsType"]}</GoodsType>\n')
                #         xml.write(f'<AvitoStatus>{card["AvitoStatus"]}</AvitoStatus>\n')
                #         if "AdStatus" in card:
                #             xml.write(f'<AdStatus>{card["AdStatus"]}</AdStatus>\n')
                #         xml.write(f'<ContactMethod>{card["ContactMethod"]}</ContactMethod>\n')
                #         xml.write(f'<ListingFee>{card["ListingFee"]}</ListingFee>\n')
                #         xml.write(f'<CompanyName>{card["CompanyName"]}</CompanyName>\n')
                #         xml.write(f'<EMail>{contacts["email"]}</EMail>\n')
                #         xml.write(f'<RimDiameter>{card["RimDiameter"]}</RimDiameter>\n')
                #         xml.write(f'<Quantity>{card["Quantity"]}</Quantity>\n')
                #         xml.write(f'<TireType>{card["TireType"]}</TireType>\n')
                #         xml.write(f'<TireAspectRatio>{card["TireAspectRatio"]}</TireAspectRatio>\n')
                #         xml.write(f'<LoadIndex>{card["LoadIndex"]}</LoadIndex>\n')
                #         xml.write(f'<DifferentWidthTires>{card["DifferentWidthTires"]}</DifferentWidthTires>\n')
                #         xml.write(f'<SpeedIndex>{card["SpeedIndex"]}</SpeedIndex>\n')
                #         xml.write(f'<RunFlat>{card["RunFlat"]}</RunFlat>\n')
                #         xml.write(f'<Model>{card["Model"]}</Model>\n')
                #         xml.write(f'<Brand>{card["Brand"]}</Brand>\n')
                #         xml.write(f'<TireSectionWidth>{card["TireSectionWidth"]}</TireSectionWidth>\n')
                #         xml.write(f'<ContactPhone>{contacts["phone"]}</ContactPhone>\n')
                #         xml.write(f'<Address>{random.choice(contacts["adress"])}</Address>\n')
                #         xml.write(f'<Title>{card["Title"].replace("&", "&amp;")}</Title>\n')
                #         xml.write(f'<Description><![CDATA[{desc.replace("%title%", card["Title"]).replace("&", "&amp;")}]]></Description>\n')
                #         xml.write(f'<Price>{card["Price"]}</Price>\n')
                #         if 'DateEnd' in card and card['DateEnd'] is not None:
                #             xml.write(f"<DateEnd>{card['DateEnd']}</DateEnd>\n")
                #         if "VideoUrl" in card and card["VideoUrl"]:
                #             xml.write(f'<VideoUrl>{card["VideoUrl"]}</VideoUrl>\n')
                #         xml.write(f'<Images>\n')
                #         for image in card['ImageUrls'].split('|'):
                #             xml.write(f'<Image url="{image.strip()}"/>\n')
                #         xml.write(f'</Images>\n')
                #         xml.write('</Ad>\n')

            xml.write('</Ads>')

    return 1
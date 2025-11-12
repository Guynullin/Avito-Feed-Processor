import random


# alloy_dict_new = {
#     '5x108.0' : 'Zeekr, Haval, LiXiang L9 (Лейсан), Chery Tiggo, Exeed, Changan, Tesla, Omoda (все модели), Hongqi (Хунци), Great Wall, Tank',
#     '5x108' : 'Zeekr, Haval, LiXiang L9 (Лейсан), Chery Tiggo, Exeed, Changan, Tesla, Omoda (все модели), Hongqi (Хунци), Great Wall, Tank',

#     '5x110.0' : 'Alfa Romeo, Dodge, Jeep, Tesla',
#     '5x110' : 'Alfa Romeo, Dodge, Jeep, Tesla',

#     '5x112.0' : 'Audi (все модели); BMW (все модели); Mercedes (все модели); Porsche Macan; Skoda Octavia; Volkswagen (все модели)',
#     '5x112' : 'Audi (все модели); BMW (все модели); Mercedes (все модели); Porsche Macan; Skoda Octavia; Volkswagen (все модели)',

#     '5x114.3' : 'Changan, Chery, Ford Mustang, Geely, Genesis, Haval H6/H7/H8, Honda, Hyundai(все модели), Infiniti, Jeep, Kia Optima, Kia Sportage, Kia K5, Land Rover, Lexus, Mazda, Mitsubishi, Nissan, Tesla Model 3, Tesla Model Y, Toyota (все модели)',

#     '5x115.0' : 'Cadillac (все модели), Chevrolet (все модели), Chrysler, Dodge, Opel (все модели)',
#     '5x115' : 'Cadillac (все модели), Chevrolet (все модели), Chrysler, Dodge, Opel (все модели)',

#     '5x120.0' : 'BMW (все модели *Series*), BMW (все модели *X*), Bentley, Land Rover (все модели), Range Rover, Lexus (все модели), Pontiac,  Volkswagen (все модели)',
#     '5x120' : 'BMW (все модели *Series*), BMW (все модели *X*), Bentley, Land Rover (все модели), Range Rover, Lexus (все модели), Pontiac,  Volkswagen (все модели)',

#     '5x127.0' : 'Cadillac, Chrysler, Dodge, Jeep (все модели)',
#     '5x127' : 'Cadillac, Chrysler, Dodge, Jeep (все модели)',

#     '5x130.0' : 'Audi (все модели), Bentley, Bugatti, Citroen, Maxus, Mercedes-Benz (все модели), Nissan, Porsche (все модели)',
#     '5x130' : 'Audi (все модели), Bentley, Bugatti, Citroen, Maxus, Mercedes-Benz (все модели), Nissan, Porsche (все модели)',

#     '5x135.0' : 'Ford (все модели), Lincoln',
#     '5x135' : 'Ford (все модели), Lincoln',

#     '5x150.0' : 'Lexus LX, Toyota Land Cruiser',
#     '5x150' : 'Lexus LX, Toyota Land Cruiser',

#     '4x98.0' : 'Ваз(лада) 2112, Ладу Гранту, Ладу Калину, Ладу Приору, Ваз(лада) 2114',
#     '4x98' : 'Ваз(лада) 2112, Ладу Гранту, Ладу Калину, Ладу Приору, Ваз(лада) 2114',

#     '4x100.0' : 'Kia Rio (Киа Рио), Hyundai Solaris (Хендай Солярис), Hyundai Accent (Хендай Акцент), Hyundai Gets (Хендай Гетс), Opel Corsa (Опель Корса), Renault Sandero (Рено Сандеро), Lada Vesta (Веста), Lada X-ray (Икс Рэй)',
#     '4x100' : 'Kia Rio (Киа Рио), Hyundai Solaris (Хендай Солярис), Hyundai Accent (Хендай Акцент), Hyundai Gets (Хендай Гетс), Opel Corsa (Опель Корса), Renault Sandero (Рено Сандеро), Lada Vesta (Веста), Lada X-ray (Икс Рэй)',

#     '4x108.0' : 'Citroen, Ford (все модели), Jeep, Opel Corsa',
#     '4x108' : 'Citroen, Ford (все модели), Jeep, Opel Corsa',

#     '4x114.3' : 'Baic, Changan, Changhe, Chery, Chevrolet, Kia, Nissan, Proton',

#     '6x139.7' : 'Cadillac Escalade (Кадиллак Эскалайд), Chery H5, Chery Transcom, Chevrolet Colorado (Шевроле), Chevrolet Tahoe, Great Wall Wingle, Haval H5, Haval H9, Infiniti, Jeep Grand Wagoneer, Lexus LX, Tank 300, Tank 500, Toyota Land Cruiser Prado, Volkswagen Amarok',

#     '5x100.0' : ' Audi (Ауди) A1/A2/A3, Chevrolet (Шевроле), Lexus (Лексус), Skoda (Шкода), Toyota (Тойота), Volkswagen (Фольксваген)',
#     '5x100' : ' Audi (Ауди) A1/A2/A3, Chevrolet (Шевроле), Lexus (Лексус), Skoda (Шкода), Toyota (Тойота), Volkswagen (Фольксваген)',
# }

# forged_dict_new = {
#     '5x108.0' : 'Zeekr, Haval, LiXiang L9 (Лейсан), Chery Tiggo, Exeed, Changan, Tesla(Тесла), Omoda (все модели), Hongqi (Хунци), Great Wall, Tank',
#     '5x108' : 'Zeekr, Haval, LiXiang L9 (Лейсан), Chery Tiggo, Exeed, Changan, Tesla(Тесла), Omoda (все модели), Hongqi (Хунци), Great Wall, Tank',

#     '5x110.0' : 'Alfa Romeo(Альфа Ромео), Dodge, Jeep, Tesla(Тесла)',
#     '5x110' : 'Alfa Romeo(Альфа Ромео), Dodge, Jeep, Tesla(Тесла)',

#     '5x112.0' : 'Audi(Ауди)-все модели; BMW (БМВ)-все модели; Mercedes (Мерседес)-все модели; Porsche-Порш Macan; Volkswagen (все модели)',
#     '5x112' : 'Audi(Ауди)-все модели; BMW (БМВ)-все модели; Mercedes (Мерседес)-все модели; Porsche-Порш Macan; Volkswagen (все модели)',

#     '5x114.3' : 'Changan (Чанган), Chery, Ford Mustang, Geely, Genesis, Haval H6/H7/H8, Honda, Hyundai(все модели), Infiniti, Jeep, Kia Optima, Kia Sportage, Kia K5, Land Rover, Lexus, Mazda, Mitsubishi, Nissan, Tesla Model 3, Tesla Model Y, Toyota (Тойота)-все модели',

#     '5x115.0' : 'Cadillac (все модели), Chevrolet (все модели), Chrysler, Dodge, Opel (все модели)',
#     '5x115' : 'Cadillac (все модели), Chevrolet (все модели), Chrysler, Dodge, Opel (все модели)',

#     '5x120.0' : 'BMW (все модели *Series*), BMW (все модели *X*), Bentley, Land Rover (все модели), Range Rover, Lexus (все модели), Pontiac,  Volkswagen (все модели)',
#     '5x120' : 'BMW (все модели *Series*), BMW (все модели *X*), Bentley, Land Rover (все модели), Range Rover, Lexus (все модели), Pontiac,  Volkswagen (все модели)',

#     '5x127.0' : 'Cadillac, Chrysler, Dodge, Jeep (все модели)',
#     '5x127' : 'Cadillac, Chrysler, Dodge, Jeep (все модели)',

#     '5x130.0' : 'Audi(Ауди)-все модели, Bentley, Bugatti, Citroen, Maxus, Mercedes-Benz (Мерседес)-все модели, Nissan, Porsche (все модели)',
#     '5x130' : 'Audi(Ауди)-все модели, Bentley, Bugatti, Citroen, Maxus, Mercedes-Benz (Мерседес)-все модели, Nissan, Porsche (все модели)',

#     '5x135.0' : 'Ford (все модели), Lincoln',
#     '5x135' : 'Ford (все модели), Lincoln',

#     '5x150.0' : 'Lexus LX, Toyota Land Cruiser',
#     '5x150' : 'Lexus LX, Toyota Land Cruiser',

#     '4x98.0' : 'Ваз(лада) 2112, Ладу Гранту, Ладу Калину, Ладу Приору, Ваз(лада) 2114',
#     '4x98' : 'Ваз(лада) 2112, Ладу Гранту, Ладу Калину, Ладу Приору, Ваз(лада) 2114',

#     '4x100.0' : 'Kia Rio (Киа Рио), Hyundai Solaris (Хендай), Hyundai Accent (Хендай Акцент), Hyundai Gets (Хендай Гетс), Opel Corsa (Опель Корса), Renault Sandero (Рено Сандеро), Lada Vesta (Веста), Lada X-ray (Икс Рэй)',
#     '4x100' : 'Kia Rio (Киа Рио), Hyundai Solaris (Хендай), Hyundai Accent (Хендай Акцент), Hyundai Gets (Хендай Гетс), Opel Corsa (Опель Корса), Renault Sandero (Рено Сандеро), Lada Vesta (Веста), Lada X-ray (Икс Рэй)',

#     '4x108.0' : 'Citroen, Ford (все модели), Jeep, Opel Corsa',
#     '4x108' : 'Citroen, Ford (все модели), Jeep, Opel Corsa',

#     '4x114.3' : 'Baic, Changan, Changhe, Chery, Chevrolet, Kia, Nissan, Proton',

#     '6x139.7' : 'Cadillac Escalade (Кадиллак Эскалайд), Chery H5, Chery Transcom, Chevrolet Colorado (Шевроле), Chevrolet Tahoe, Great Wall Wingle, Haval H5, Haval H9, Infiniti, Jeep Grand Wagoneer, Lexus LX, Tank 300, Tank 500, Toyota Land Cruiser Prado, Volkswagen Amarok',
    
#     '5x100.0' : ' Audi (Ауди) A1/A2/A3, Chevrolet (Шевроле), Lexus (Лексус), Skoda (Шкода), Toyota (Тойота), Volkswagen (Фольксваген)',
#     '5x100' : ' Audi (Ауди) A1/A2/A3, Chevrolet (Шевроле), Lexus (Лексус), Skoda (Шкода), Toyota (Тойота), Volkswagen (Фольксваген)'

# }


PCD_DICT = {
  "10x100.0/108.0%73.1$18": "Данный комплект дисков со сверловкой 10x100.0/108.0 подойдет на VOLKSWAGEN Polo.",
  "10x100.0/112.0%66.6$17": "Данный комплект дисков со сверловкой 10x100.0/112.0 подойдет на AUDI A6.",
  "10x100.0/112.0%66.6$18": "Данный комплект дисков со сверловкой 10x100.0/112.0 подойдет на MERCEDES V-Klasse.",
  "10x100.0/112.0%73.1$18": "Данный комплект дисков со сверловкой 10x100.0/112.0 подойдет на AUDI A3, SKODA Octavia, VOLKSWAGEN Golf VI.",
  "10x100.0/113.0%73.1$17": "Данный комплект дисков со сверловкой 10x100.0/113.0 подойдет на KIA Ceed, MAZDA 3, SKODA Rapid, TOYOTA Auris, TOYOTA Corolla, VOLKSWAGEN Polo.",
  "10x100.0/114.3%67.1$17": "Данный комплект дисков со сверловкой 10x100.0/114.3 подойдет на MITSUBISHI ASX.",
  "10x100.0/114.3%73.1$15": "Данный комплект дисков со сверловкой 10x100.0/114.3 подойдет на ГАЗ Соболь.",
  "10x100.0/114.3%73.1$16": "Данный комплект дисков со сверловкой 10x100.0/114.3 подойдет на Exeed TXL, HONDA Civic, MAZDA 3, MITSUBISHI Lancer, SKODA Rapid, SUBARU Forester, SUZUKI Grand Vitara, TOYOTA Corolla, TOYOTA Crown, VOLKSWAGEN Polo.",
  "10x100.0/114.3%73.1$17": "Данный комплект дисков со сверловкой 10x100.0/114.3 подойдет на AUDI A1, BMW 5-series, HONDA Accord, HONDA CR-V, HONDA Civic, HYUNDAI Elantra, KIA Ceed, KIA Cerato, MAZDA 3, MITSUBISHI Galant, MITSUBISHI Lancer, NISSAN Juke, NISSAN Teana, PONTIAC Vibe, RENAULT Duster, SKODA Rapid, SUBARU Forester, SUBARU Impreza, SUBARU Legacy, TOYOTA Avensis, TOYOTA Corolla, TOYOTA GT 86, TOYOTA RAV 4, TOYOTA Wish, VOLKSWAGEN Jetta, VOLKSWAGEN Polo.",
  "10x100.0/114.3%73.1$18": "Данный комплект дисков со сверловкой 10x100.0/114.3 подойдет на CHANGAN CS55 Plus, FAW Besturn B30, HONDA Accord, HONDA Civic, HYUNDAI Elantra, KIA Ceed, KIA K5, KIA Stinger, LEXUS CT, LEXUS ES, MAZDA 3, MAZDA MPV, MITSUBISHI Eclipse, MITSUBISHI Lancer, RENAULT Duster, SUBARU Forester, SUBARU Impreza, SUBARU Legacy, SUBARU XV, SUZUKI SX4, TOYOTA Avensis, TOYOTA Camry, TOYOTA Corolla, TOYOTA Crown, TOYOTA GT 86, VOLKSWAGEN Golf VII, VOLKSWAGEN Polo.",
  "10x105.0/114.3%73.1$17": "Данный комплект дисков со сверловкой 10x105.0/114.3 подойдет на CHEVROLET Cruze, MERCEDES C-Klasse.",
  "10x108.0/112.0%66.6$18": "Данный комплект дисков со сверловкой 10x108.0/112.0 подойдет на SKODA Octavia.",
  "10x108.0/112.0%73.1$16": "Данный комплект дисков со сверловкой 10x108.0/112.0 подойдет на AUDI A4, CHERY Tiggo 4, FORD C-Max, FORD Focus, SKODA Octavia, VOLKSWAGEN Jetta.",
  "10x108.0/112.0%73.1$17": "Данный комплект дисков со сверловкой 10x108.0/112.0 подойдет на AUDI A4 Allroad, CHANGAN CS35, FORD Focus, FORD Kuga, FORD Mondeo, OPEL Astra H, PEUGEOT 508, SKODA Octavia, VOLKSWAGEN Jetta.",
  "10x108.0/112.0%73.1$18": "Данный комплект дисков со сверловкой 10x108.0/112.0 подойдет на CHERY Arrizo 8, FORD Focus, FORD Mondeo, MERCEDES E-Klasse, SKODA Octavia.",
  "10x108.0/112.0%73.1$19": "Данный комплект дисков со сверловкой 10x108.0/112.0 подойдет на VOLKSWAGEN Tiguan.",
  "10x108.0/113.0%73.1$17": "Данный комплект дисков со сверловкой 10x108.0/113.0 подойдет на FORD Focus, HONDA Civic, MAZDA 6, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII.",
  "10x108.0/113.0%73.1$18": "Данный комплект дисков со сверловкой 10x108.0/113.0 подойдет на AUDI A4, AUDI TT RS, BMW 3-series, CHERY Arrizo 8, CHERY Tiggo 7 Pro, Exceed TXL, FORD Focus, FORD Mondeo, GEELY Coolray, HONDA Accord, HONDA Civic, JAECOO J7, KIA Optima, KIA Sorento Prime, KIA Soul, KIA Stinger, LEXUS IS, MAZDA 3, MERCEDES E-Klasse, MERCEDES GLA-Klasse, MITSUBISHI Lancer, MITSUBISHI Outlander, NISSAN Skyline, NISSAN Teana, OPEL Astra H, RENAULT Arkana, TOYOTA Alphard, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC, VOLVO S60.",
  "10x108.0/113.0%73.1$19": "Данный комплект дисков со сверловкой 10x108.0/113.0 подойдет на AUDI Q5, CHERY Tiggo 7 PRO, GAC GS4 Coupe, GEELY Atlas, JAECOO J7, KIA K5, KIA Optima, MAZDA CX-5, VOLKSWAGEN Teramont.",
  "10x108.0/113.0%73.1$20": "Данный комплект дисков со сверловкой 10x108.0/113.0 подойдет на Exceed RX, Exeed VX, GEELY MONJARO, HAVAL F7, HYUNDAI Santa Fe, Jetour T2, NISSAN Pixo, TOYOTA Highlander, VOLKSWAGEN Teramont.",
  "10x108.0/114.3%65.1$18": "Данный комплект дисков со сверловкой 10x108.0/114.3 подойдет на PEUGEOT Traveller.",
  "10x108.0/114.3%67.1$22": "Данный комплект дисков со сверловкой 10x108.0/114.3 подойдет на Exeed VX.",
  "10x108.0/114.3%73.1$18": "Данный комплект дисков со сверловкой 10x108.0/114.3 подойдет на CHANGAN UNI-V, CHERY Tiggo 7 PRO, FORD Focus, HYUNDAI Santa Fe, KIA Ceed, OPEL Astra H, Omoda C5, SUBARU Outback, TOYOTA Camry, TOYOTA Corolla.",
  "10x108.0/114.3%73.1$20": "Данный комплект дисков со сверловкой 10x108.0/114.3 подойдет на CHERY Tiggo 9, Exceed TXL, Exeed LX, Exeed VX, GEELY MONJARO, GEELY Monjaro, HAVAL Dargo, JAECOO J7, JAGUAR XJ, Jetour X95, KIA Sportage, LEXUS RX, TOYOTA RAV 4, VOLVO XC90, Zeekr 9.",
  "10x108.0/120.0%72.6$22": "Данный комплект дисков со сверловкой 10x108.0/120.0 подойдет на LAND ROVER Range Rover.",
  "10x108.0/120.0%73.1$21": "Данный комплект дисков со сверловкой 10x108.0/120.0 подойдет на Exceed TXL.",
  "10x112.0/114.3%73.1$18": "Данный комплект дисков со сверловкой 10x112.0/114.3 подойдет на KIA Cerato, SKODA Superb, VOLKSWAGEN Scirocco.",
  "10x112.0/120.0%73.1$18": "Данный комплект дисков со сверловкой 10x112.0/120.0 подойдет на BMW 3-series, VOLKSWAGEN Golf VII.",
  "10x113.0/108.0%73.1$19": "Данный комплект дисков со сверловкой 10x113.0/108.0 подойдет на Exceed RX, HONDA CR-V, KIA Sorento, LAND ROVER Freelander, MERCEDES GLS-Klasse, VOLVO S90.",
  "10x113.0/108.0%73.1$20": "Данный комплект дисков со сверловкой 10x113.0/108.0 подойдет на CHERY Tiggo 5, GEELY MONJARO, GEELY Monjaro, INFINITI FX37, JAGUAR F-Pace, NISSAN Pixo, NISSAN X-Trail.",
  "10x114.3/120.0%74.1$18": "Данный комплект дисков со сверловкой 10x114.3/120.0 подойдет на VOLKSWAGEN Amarok.",
  "10x114.3/120.0%74.1$17": "Данный комплект дисков со сверловкой 10x114.3/120.0 подойдет на MAZDA 3, MITSUBISHI Lancer, RENAULT Arkana, VOLKSWAGEN Multivan.",
  "10x120.0/127.0%74.1$17": "Данный комплект дисков со сверловкой 10x120.0/127.0 подойдет на VOLKSWAGEN Amarok.",
  "10x120.0/127.0%75$20": "Данный комплект дисков со сверловкой 10x120.0/127.0 подойдет на VOLKSWAGEN Amarok.",
  "10x127.0/139.7%87.1$20": "Данный комплект дисков со сверловкой 10x127.0/139.7 подойдет на JEEP Wrangler.",
  "10x139.7/150.0%110$18": "Данный комплект дисков со сверловкой 10x139.7/150.0 подойдет на LADA Niva, УАЗ 3163* Patriot.",
  "10x139.7/150.0%110.1$16": "Данный комплект дисков со сверловкой 10x139.7/150.0 подойдет на LADA Niva, УАЗ 3163* Patriot.",
  "10x139.7/150.0%110.1$18": "Данный комплект дисков со сверловкой 10x139.7/150.0 подойдет на УАЗ 3163* Patriot.",
  "10x139.7/150.0%110.1$20": "Данный комплект дисков со сверловкой 10x139.7/150.0 подойдет на УАЗ 3163* Patriot, УАЗ 3741*, УАЗ Профи.",
  "10x139.0/150.0%110$16": "Данный комплект дисков со сверловкой 10x139.0/150.0 подойдет на CHEVROLET Niva.",
  "10x139.0/150.0%110$18": "Данный комплект дисков со сверловкой 10x139.0/150.0 подойдет на УАЗ 3163* Patriot.",
  "10x139.0/150.0%110.1$16": "Данный комплект дисков со сверловкой 10x139.0/150.0 подойдет на УАЗ 3163* Patriot, УАЗ 3164 Patriot Sport.",
  "10x139.0/150.0%110.1$20": "Данный комплект дисков со сверловкой 10x139.0/150.0 подойдет на TOYOTA Tundra.",
  "10x139.0/150.0%110.2$20": "Данный комплект дисков со сверловкой 10x139.0/150.0 подойдет на TOYOTA Land Cruiser 200.",
  "10x139.0/150.0%110.5$20": "Данный комплект дисков со сверловкой 10x139.0/150.0 подойдет на TOYOTA Tundra, УАЗ 3163* Patriot.",
  "12x130.0/135.0%87.1$17": "Данный комплект дисков со сверловкой 12x130.0/135.0 подойдет на MERCEDES Sprinter.",
  "12x135.0/139.7%106.1$20": "Данный комплект дисков со сверловкой 12x135.0/139.7 подойдет на Tank 300.",
  "12x135.0/139.7%110$18": "Данный комплект дисков со сверловкой 12x135.0/139.7 подойдет на DODGE Ram 1500, Tank 300.",
  "12x135.0/139.7%110.1$18": "Данный комплект дисков со сверловкой 12x135.0/139.7 подойдет на Tank 300.",
  "12x135.0/139.7%110.1$20": "Данный комплект дисков со сверловкой 12x135.0/139.7 подойдет на FORD F-150.",
  "12x135.0/139.7%110.5$18": "Данный комплект дисков со сверловкой 12x135.0/139.7 подойдет на TOYOTA Land Cruiser Prado.",
  "12x135.0/139.7%110.5$20": "Данный комплект дисков со сверловкой 12x135.0/139.7 подойдет на FORD Ranger, TOYOTA Land Cruiser Prado.",
  "12x135.0/139.7%87.1$24": "Данный комплект дисков со сверловкой 12x135.0/139.7 подойдет на LINCOLN Navigator.",
  "4x100.0%54.1$15": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, TOYOTA bB.",
  "4x100.0%54.1$16": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio.",
  "4x100.0%54.1$18": "Данный комплект дисков со сверловкой 4x100.0 подойдет на KIA Rio.",
  "4x100.0%56.1$15": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HONDA Freed/Freed Spike.",
  "4x100.0%56.1$16": "Данный комплект дисков со сверловкой 4x100.0 подойдет на KIA Rio.",
  "4x100.0%56.6$14": "Данный комплект дисков со сверловкой 4x100.0 подойдет на DAEWOO Nexia.",
  "4x100.0%60.1$15": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Priora, LADA Vesta, LADA X-Ray, RENAULT Logan.",
  "4x100.0%60.1$16": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Granta, LADA Priora, LADA Vesta, RENAULT Sandero.",
  "4x100.0%60.1$17": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Granta, LADA Kalina, LADA Priora, LADA Vesta, LADA X-Ray, TOYOTA Raum.",
  "4x100.0%60.1$18": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Vesta, NISSAN Almera.",
  "4x100.0%67.0$14": "Данный комплект дисков со сверловкой 4x100.0 подойдет на NISSAN Note.",
  "4x100.0%67.0$16": "Данный комплект дисков со сверловкой 4x100.0 подойдет на NISSAN Note.",
  "4x100.0%67.0$17": "Данный комплект дисков со сверловкой 4x100.0 подойдет на LADA Granta, LADA Kalina, LADA Vesta.",
  "4x100.0%67.1$14": "Данный комплект дисков со сверловкой 4x100.0 подойдет на CHEVROLET Aveo, MITSUBISHI Space Star, TOYOTA Yaris.",
  "4x100.0%67.1$15": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Granta, LADA Priora, LADA Vesta.",
  "4x100.0%67.1$16": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, LADA Largus, RENAULT Logan, RENAULT Sandero.",
  "4x100.0%67.1$17": "Данный комплект дисков со сверловкой 4x100.0 подойдет на KIA Rio, LADA Granta, LADA Vesta.",
  "4x100.0%67.1$14": "Данный комплект дисков со сверловкой 4x100.0 подойдет на LADA Granta.",
  "4x100.0%67.1$15": "Данный комплект дисков со сверловкой 4x100.0 подойдет на CHEVROLET Aveo, HYUNDAI Solaris, KIA Rio, KIA Rio X, LADA Granta, LADA Largus, TOYOTA CYNOS.",
  "4x100.0%67.1$16": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Granta, LADA Kalina, LADA Vesta.",
  "4x100.0%67.1$17": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Vesta, RENAULT Sandero, SMART Fortwo.",
  "4x100.0%73.1$14": "Данный комплект дисков со сверловкой 4x100.0 подойдет на CHEVROLET Spark, LADA Kalina, NISSAN Leaf.",
  "4x100.0%73.1$15": "Данный комплект дисков со сверловкой 4x100.0 подойдет на CHERY Bonus, CHEVROLET Aveo, CHEVROLET Cobalt, DAEWOO Nexia, HONDA Airwave, HONDA Fit, HONDA Freed/Freed Spike, HYUNDAI Accent Tagaz, HYUNDAI Getz, HYUNDAI Solaris, KIA Picanto, KIA Rio, KIA Spectra, LADA Granta, LADA Kalina, LADA Largus, LADA Priora, LADA Vesta, LADA X-Ray, MAZDA 2/Demio, NISSAN Almera, NISSAN Note, PEUGEOT 107, RENAULT Logan, RENAULT Sandero, SUZUKI Swift, TOYOTA CYNOS, TOYOTA Succeed/Probox, TOYOTA Vitz, TOYOTA Yaris, TOYOTA bB.",
  "4x100.0%73.1$16": "Данный комплект дисков со сверловкой 4x100.0 подойдет на CHEVROLET Aveo, CHEVROLET Spark, DAEWOO Nexia, DATSUN Mi-Do, DATSUN On-Do, HONDA Fit, HONDA Fit Shuttle, HONDA Freed/Freed Spike, HYUNDAI Accent Tagaz, HYUNDAI Getz, HYUNDAI Solaris, KIA Ceed, KIA Picanto, KIA Rio, KIA Rio X, KIA Rio X-Line, KIA Spectra, LADA Granta, LADA Kalina, LADA Kalina NFR, LADA Largus, LADA Priora, LADA Samara, LADA Vesta, LADA X-Ray, LIFAN Celliya, LIFAN Smily, LIFAN Solano, MAZDA 2/Demio, MINI Hatch, NISSAN Almera, NISSAN Cube, NISSAN Note, OPEL Corsa D, PEUGEOT 107, PEUGEOT 308, RENAULT Logan, RENAULT Logan Stepway, RENAULT Megane II, RENAULT Sandero, RENAULT Sandero Stepway, SMART Fortwo, SUZUKI Swift, TOYOTA Corolla Fielder, TOYOTA Ractis, TOYOTA Vitz, TOYOTA Yaris.",
  "4x100.0%73.1$17": "Данный комплект дисков со сверловкой 4x100.0 подойдет на CITROEN C4, DAEWOO Nexia, DATSUN On-Do, FIAT Albea, HONDA Fit, HONDA Freed/Freed Spike, HYUNDAI Accent Tagaz, HYUNDAI Getz, HYUNDAI Solaris, KIA Rio, KIA Rio X, KIA Rio X-Line, KIA Spectra, LADA Granta, LADA Kalina, LADA Largus, LADA Priora, LADA Samara, LADA Vesta, LADA X-Ray, LIFAN Solano, LIFAN Solano II, MINI Hatch, NISSAN Almera, NISSAN Almera Classic, NISSAN Cube, NISSAN Note, OPEL Astra H, OPEL Corsa D, RENAULT Clio IV, RENAULT Logan, RENAULT Megane II, RENAULT Sandero, RENAULT Sandero Stepway, TOYOTA Corolla Fielder, TOYOTA Raum, TOYOTA Yaris, TOYOTA bB.",
  "4x100.0%73.1$18": "Данный комплект дисков со сверловкой 4x100.0 подойдет на HYUNDAI Solaris, KIA Rio, KIA Rio X-Line, LADA Vesta.",
  "4x100.0/114.0,3.0%73.1$14": "Данный комплект дисков со сверловкой 4x100.0/114.0,3.0 подойдет на LADA Granta, LADA Priora, NISSAN Cube.",
  "4x100.0/114.0,3.0%73.1$15": "Данный комплект дисков со сверловкой 4x100.0/114.0,3.0 подойдет на CHEVROLET Lacetti, LADA Granta, LADA Kalina, NISSAN Almera Classic, OPEL Corsa D.",
  "4x100.0/114.0,3.0%73.1$16": "Данный комплект дисков со сверловкой 4x100.0/114.0,3.0 подойдет на CHEVROLET Lacetti, HYUNDAI Solaris, LADA Vesta, NISSAN Almera Classic.",
  "4x100.0/114.0,3.0%73.1$17": "Данный комплект дисков со сверловкой 4x100.0/114.0,3.0 подойдет на CHEVROLET Lacetti, LADA Granta, LADA X-Ray, MITSUBISHI Galant.",
  "4x100.0/114.0,3.0%73.1$18": "Данный комплект дисков со сверловкой 4x100.0/114.0,3.0 подойдет на FIAT Bravo II.",
  "4x108.0%63.4$15": "Данный комплект дисков со сверловкой 4x108.0 подойдет на FORD Fiesta.",
  "4x108.0%65.1$15": "Данный комплект дисков со сверловкой 4x108.0 подойдет на PEUGEOT Partner.",
  "4x108.0%73.1$16": "Данный комплект дисков со сверловкой 4x108.0 подойдет на CITROEN C3, CITROEN C4, FORD Fusion.",
  "4x108.0%73.1$17": "Данный комплект дисков со сверловкой 4x108.0 подойдет на CITROEN C4.",
  "4x114.3%67.1$16": "Данный комплект дисков со сверловкой 4x114.3 подойдет на NISSAN Almera Classic.",
  "4x114.3%73.1$15": "Данный комплект дисков со сверловкой 4x114.3 подойдет на CHEVROLET Lacetti, NISSAN Almera Classic.",
  "4x114.3%73.1$16": "Данный комплект дисков со сверловкой 4x114.3 подойдет на CHEVROLET Lacetti, NISSAN Almera Classic.",
  "4x114.3%73.1$17": "Данный комплект дисков со сверловкой 4x114.3 подойдет на CHEVROLET Lacetti, DAEWOO Gentra, HYUNDAI Sonata, NISSAN Tiida.",
  "4x98.0%58.5$13": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta.",
  "4x98.0%58.5$14": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta, LADA Priora.",
  "4x98.0%58.5$15": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta, LADA Vesta.",
  "4x98.0%58.5$16": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta, LADA Priora.",
  "4x98.0%58.6$14": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta.",
  "4x98.0%58.6$15": "Данный комплект дисков со сверловкой 4x98.0 подойдет на FIAT Doblo, LADA Granta, LADA Kalina, LADA Priora, LADA Vesta.",
  "4x98.0%58.6$16": "Данный комплект дисков со сверловкой 4x98.0 подойдет на DATSUN On-Do, LADA Granta, LADA Kalina, LADA Priora.",
  "4x98.0%58.6$17": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta, LADA Kalina, LADA Largus, LADA Priora.",
  "4x98.0%67.0$14": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Priora.",
  "4x98.0%67.1$14": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta.",
  "4x98.0%67.1$15": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta, LADA Kalina.",
  "4x98.0%73.1$14": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Samara.",
  "4x98.0%73.1$15": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta, LADA Kalina, LADA Priora, LADA Vesta.",
  "4x98.0%73.1$16": "Данный комплект дисков со сверловкой 4x98.0 подойдет на LADA Granta, LADA Vesta.",
  "5X100/5X114.3%73.1$17": "Данный комплект дисков со сверловкой 5X100/5X114.3 подойдет на SUBARU Impreza, TOYOTA C-HR, VOLKSWAGEN Polo.",
  "5x100.0%56.1$18": "Данный комплект дисков со сверловкой 5x100.0 подойдет на SUBARU Impreza WRX.",
  "5x100.0%57.1$14": "Данный комплект дисков со сверловкой 5x100.0 подойдет на SKODA Rapid.",
  "5x100.0%57.1$15": "Данный комплект дисков со сверловкой 5x100.0 подойдет на SKODA Rapid, VOLKSWAGEN Polo.",
  "5x100.0%57.1$16": "Данный комплект дисков со сверловкой 5x100.0 подойдет на SKODA Rapid, TOYOTA Avensis, TOYOTA Corolla, VOLKSWAGEN Polo.",
  "5x100.0%57.1$17": "Данный комплект дисков со сверловкой 5x100.0 подойдет на AUDI A1, SKODA Rapid, SUBARU Forester, TOYOTA Wish, VOLKSWAGEN Polo.",
  "5x100.0%67.1$17": "Данный комплект дисков со сверловкой 5x100.0 подойдет на VOLKSWAGEN Polo.",
  "5x100.0%67.1$16": "Данный комплект дисков со сверловкой 5x100.0 подойдет на AUDI A1, SKODA Rapid, VOLKSWAGEN Polo.",
  "5x100.0%67.1$17": "Данный комплект дисков со сверловкой 5x100.0 подойдет на SKODA Rapid, SUBARU Forester, VOLKSWAGEN Polo.",
  "5x100.0%73.1$15": "Данный комплект дисков со сверловкой 5x100.0 подойдет на SKODA Fabia, SKODA Rapid, TOYOTA Sienna, VOLKSWAGEN Polo.",
  "5x100.0%73.1$16": "Данный комплект дисков со сверловкой 5x100.0 подойдет на AUDI A1, CHRYSLER PT Cruiser, FIAT Doblo, GEELY MONJARO, SKODA Fabia, SKODA Rapid, SKODA Roomster, SUBARU Forester, TOYOTA Allion/Premio, TOYOTA Avensis, TOYOTA Corolla, TOYOTA Prius, TOYOTA Sienna, VOLKSWAGEN Polo.",
  "5x100.0%73.1$17": "Данный комплект дисков со сверловкой 5x100.0 подойдет на CHRYSLER PT Cruiser, PONTIAC Vibe, SKODA Rapid, SUBARU BRZ, SUBARU Forester, SUBARU Impreza, SUBARU Impreza WRX, SUBARU Impreza XV, SUBARU WRX, SUBARU XV, TOYOTA Allion/Premio, TOYOTA Avensis, TOYOTA Corolla, TOYOTA Prius, TOYOTA Sienna, TOYOTA Wish, VOLKSWAGEN Polo.",
  "5x100.0%73.1$18": "Данный комплект дисков со сверловкой 5x100.0 подойдет на AUDI A1, SKODA Rapid, SUBARU BRZ, SUBARU Forester, SUBARU Legacy, TOYOTA Corolla, TOYOTA Prius, VOLKSWAGEN Polo.",
  "5x100.0%73.1$19": "Данный комплект дисков со сверловкой 5x100.0 подойдет на SUBARU Forester, TOYOTA Corolla.",
  "5x105.0%56.6$16": "Данный комплект дисков со сверловкой 5x105.0 подойдет на CHEVROLET Cruze.",
  "5x105.0%56.6$17": "Данный комплект дисков со сверловкой 5x105.0 подойдет на CHEVROLET Aveo, CHEVROLET Cruze, OPEL Astra J.",
  "5x105.0%56.6$18": "Данный комплект дисков со сверловкой 5x105.0 подойдет на BAIC E150, CHEVROLET Cruze, CHEVROLET Trax, OPEL Astra J.",
  "5x105.0%67.1$17": "Данный комплект дисков со сверловкой 5x105.0 подойдет на OPEL Astra J.",
  "5x105.0%73.1$17": "Данный комплект дисков со сверловкой 5x105.0 подойдет на CHEVROLET Aveo, CHEVROLET Cruze, CHEVROLET Volt, OPEL Astra J, OPEL Mokka.",
  "5x105.0%73.1$18": "Данный комплект дисков со сверловкой 5x105.0 подойдет на CHEVROLET Cruze, OPEL Astra J, OPEL Mokka.",
  "5x108.0%56.6$17": "Данный комплект дисков со сверловкой 5x108.0 подойдет на OPEL Astra J.",
  "5x108.0%60.1$17": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 7.",
  "5x108.0%60.1$18": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo, CHERY Tiggo 4, CHERY Tiggo 7 PRO, CHERY Tiggo 8 Pro, Exceed TXL, Exeed LX, Omoda C5.",
  "5x108.0%60.1$19": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 7 PRO.",
  "5x108.0%60.1$20": "Данный комплект дисков со сверловкой 5x108.0 подойдет на Jetour T2.",
  "5x108.0%63.3$16": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD Focus.",
  "5x108.0%63.3$17": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD Focus.",
  "5x108.0%63.3$20": "Данный комплект дисков со сверловкой 5x108.0 подойдет на GEELY Monjaro, LAND ROVER Range Rover Evoque.",
  "5x108.0%63.3$22": "Данный комплект дисков со сверловкой 5x108.0 подойдет на Jetour X90, Zeekr 1.",
  "5x108.0%63.4$16": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD Focus.",
  "5x108.0%63.4$17": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD C-Max, FORD Focus, GEELY Monjaro, JAGUAR XF, LAND ROVER Freelander.",
  "5x108.0%63.4$18": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 7, FORD Focus, GEELY Monjaro, GEELY Tugella, Jetour X70 Plus, LAND ROVER Freelander, LAND ROVER Range Rover Evoque, Omoda C5.",
  "5x108.0%63.4$19": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 7 Pro, FORD Kuga, GEELY Atlas, GEELY Monjaro, GEELY Tugella, JAGUAR XE, JAGUAR XJ, Omoda C5, VOLVO S80.",
  "5x108.0%63.4$20": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 8 Pro, CHERY Tiggo 9, GEELY Atlas, GEELY MONJARO, GEELY Monjaro, GEELY Tugella, JAGUAR E-Pace, JAGUAR F-Type, JAGUAR XF, JAGUAR XJ, Jetour Dasheng, LAND ROVER Range Rover Evoque, LAND ROVER Range Rover Velar, Omoda C5, VOLVO XC90, Zeekr 1, Zeekr 9.",
  "5x108.0%63.4$21": "Данный комплект дисков со сверловкой 5x108.0 подойдет на GEELY Monjaro, GEELY Tugella, JAGUAR XJ, LAND ROVER Range Rover Velar, VOLVO V90 Cross Country, VOLVO XC60.",
  "5x108.0%63.4$22": "Данный комплект дисков со сверловкой 5x108.0 подойдет на LAND ROVER Range Rover, LAND ROVER Range Rover Velar, Zeekr 1.",
  "5x108.0%65.1$16": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD Focus.",
  "5x108.0%65.1$18": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Arrizo 5, CHERY Arrizo 8, GEELY Monjaro.",
  "5x108.0%65.1$19": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Arrizo 8, CHERY Tiggo 8 Pro, Exceed TXL, Exeed TXL, FORD Mondeo, GEELY Tugella, JAGUAR XF, LAND ROVER Range Rover Evoque, Omoda C5.",
  "5x108.0%65.1$20": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 7 PRO, CHERY Tiggo 8 Pro, CHERY Tiggo 9, Exceed RX, Exceed TXL, Exeed VX, FORD Edge, GEELY MONJARO, GEELY Monjaro, JAECOO J7, Jetour Dasheng, Jetour T2, VOLVO XC60, Zeekr 9.",
  "5x108.0%65.1$21": "Данный комплект дисков со сверловкой 5x108.0 подойдет на Exceed RX, Exeed LX.",
  "5x108.0%65.1$22": "Данный комплект дисков со сверловкой 5x108.0 подойдет на JAECOO J7, Zeekr 1.",
  "5x108.0%67.0$16": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD C-Max.",
  "5x108.0%67.0$18": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CITROEN C5.",
  "5x108.0%67.1$17": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD Focus.",
  "5x108.0%67.1$18": "Данный комплект дисков со сверловкой 5x108.0 подойдет на FORD Kuga, FORD S-Max, GEELY MONJARO, Omoda C5.",
  "5x108.0%67.1$20": "Данный комплект дисков со сверловкой 5x108.0 подойдет на Jetour T2.",
  "5x108.0%67.1$16": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 4, FORD Focus.",
  "5x108.0%67.1$17": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 4, FORD Focus, FORD Focus ST.",
  "5x108.0%67.1$18": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Arrizo 5, CHERY Tiggo 7 PRO, CITROEN C5, FORD Focus, LAND ROVER Freelander.",
  "5x108.0%67.1$20": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 5, CHERY Tiggo 9, GEELY Monjaro.",
  "5x108.0%73.1$16": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Tiggo 4, FORD Focus, FORD Focus ST, JAGUAR F-Pace, PEUGEOT Traveller.",
  "5x108.0%73.1$17": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Arrizo 8, CHERY Tiggo 4, CHERY Tiggo 8, DONGFENG AX7, FORD C-Max, FORD Focus, FORD Focus ST, FORD Kuga, FORD Mondeo, GEELY Monjaro, JAGUAR F-Type, JAGUAR XF, Kaiyi E5, LAND ROVER Freelander, Omoda C5, Omoda Omoda C5, PEUGEOT 3 008, PEUGEOT 407, PEUGEOT 508, VOLVO C30, VOLVO S60, VOLVO S80, VOLVO S90, VOLVO XC60, VOLVO XC70, VOLVO XC90.",
  "5x108.0%73.1$18": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Arrizo 8, CHERY Tiggo 4, CHERY Tiggo 7, CHERY Tiggo 7 PRO, CHERY Tiggo 7 Pro, CHERY Tiggo 8, CHERY Tiggo 8 Pro, CITROEN C5, Exceed TXL, FORD C-Max, FORD Focus, FORD Focus ST, FORD Kuga, FORD Mondeo, FORD S-Max, GAC GS4 Coupe, GAC GS4 PHEV, GAC GS5, GAC Trumpchi GS3, GEELY Atlas, GEELY MONJARO, GEELY Monjaro, GEELY Tugella, JAC J3, JAC J5, JAC J6, JAECOO J7, JAGUAR XE, JAGUAR XF, Jetour Dasheng, Jetour X70 Plus, Kaiyi E5, LADA Niva, OPEL Astra H, Omoda C5, Omoda Omoda C5, PEUGEOT 308, PEUGEOT 407, PEUGEOT 508, PEUGEOT Expert, VOLKSWAGEN Golf VII, VOLVO C30, VOLVO S40, VOLVO S60, VOLVO S80, VOLVO S90, VOLVO XC70, VOLVO XC90.",
  "5x108.0%73.1$19": "Данный комплект дисков со сверловкой 5x108.0 подойдет на CHERY Arrizo 3, CHERY Arrizo 8, CHERY Tiggo, CHERY Tiggo 7 PRO, CHERY Tiggo 7 Pro, CHERY Tiggo 8 Pro, Exceed RX, Exceed TXL, Exeed LX, Exeed TXL, Exeed VX, FORD Edge, FORD Focus, FORD Kuga, FORD Mondeo, FORD S-Max, GAC GS4 Coupe, GAC GS4 PHEV, GAC GS5, GAC Trumpchi GS3, GEELY Atlas, GEELY MONJARO, GEELY Monjaro, GEELY Tugella, JAC S5, JAECOO J7, JAGUAR XF, Jetour Dasheng, Jetour T2, LADA Niva, LAND ROVER Freelander, LAND ROVER Range Rover Evoque, Omoda C5, PEUGEOT 508, VOLKSWAGEN Golf VII, VOLVO S60, VOLVO S80, VOLVO V90 Cross Country, VOLVO XC60, VOLVO XC70, VOLVO XC90, Zeekr X.",
  "5x108.0%73.1$20": "Данный комплект дисков со сверловкой 5x108.0 подойдет на BMW 3-series, CHERY Tiggo 7 PRO, CHERY Tiggo 7 Pro, CHERY Tiggo 8, CHERY Tiggo 8 Pro, CHERY Tiggo 9, Exceed RX, Exceed TXL, Exeed LX, Exeed VX, FORD Focus, GEELY Atlas, GEELY MONJARO, GEELY Monjaro, GEELY Tugella, JAECOO J7, JAGUAR I-Pace, JAGUAR XJ, Jetour Dasheng, Jetour T2, Jetour Traveler, Jetour Х90Plus, LAND ROVER Freelander, LAND ROVER Range Rover Evoque, LAND ROVER Range Rover Velar.",
  "5x108.0%73.1$21": "Данный комплект дисков со сверловкой 5x108.0 подойдет на JAGUAR F-Type, Jetour T2.",
  "5x108.0%73.1$22": "Данный комплект дисков со сверловкой 5x108.0 подойдет на Zeekr 1.",
  "5x110.0%63.3$18": "Данный комплект дисков со сверловкой 5x110.0 подойдет на CHANGAN CS35 Plus.",
  "5x110.0%63.4$18": "Данный комплект дисков со сверловкой 5x110.0 подойдет на CHANGAN CS35.",
  "5x110.0%73.1$16": "Данный комплект дисков со сверловкой 5x110.0 подойдет на OPEL Astra H, Omoda Omoda C5.",
  "5x110.0%73.1$17": "Данный комплект дисков со сверловкой 5x110.0 подойдет на OPEL Astra H.",
  "5x112.0%57.1$16": "Данный комплект дисков со сверловкой 5x112.0 подойдет на SKODA Octavia, SKODA Yeti, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC, VOLKSWAGEN Tiguan.",
  "5x112.0%57.1$17": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, AUDI A7, AUDI TT, SKODA Karoq, SKODA Octavia, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan.",
  "5x112.0%57.1$18": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A6, AUDI Q3, SKODA Karoq, SKODA Kodiaq, SKODA Octavia, SKODA Superb, SKODA Yeti, TOYOTA Corolla, VOLKSWAGEN Arteon, VOLKSWAGEN Beetle, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Tiguan.",
  "5x112.0%57.1$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q3, BMW X6, SKODA Kodiaq, SKODA Octavia, SKODA Superb, VOLKSWAGEN Golf VII, VOLKSWAGEN ID.3, VOLKSWAGEN Passat, VOLKSWAGEN Scirocco, VOLKSWAGEN TAVENDOR, VOLKSWAGEN Tiguan.",
  "5x112.0%57.1$20": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q3, VOLKSWAGEN Golf VIII, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan.",
  "5x112.0%57.1$21": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q6, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan.",
  "5x112.0%57.1$22": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q5, AUDI Q7.",
  "5x112.0%66.5$16": "Данный комплект дисков со сверловкой 5x112.0 подойдет на LADA Niva.",
  "5x112.0%66.5$17": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, AUDI A4, AUDI A5, MERCEDES A-Klasse, MERCEDES C-Klasse, MERCEDES CLS-Klasse, MERCEDES E-Klasse, MERCEDES GLC-Klasse, OPEL Astra Family H, SKODA Karoq, SKODA Octavia, SKODA Octavia RS, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat.",
  "5x112.0%66.5$18": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A4, AUDI A5, AUDI Q5, MERCEDES C-Klasse, SKODA Octavia.",
  "5x112.0%66.5$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, AUDI A4, AUDI A6, AUDI A7, AUDI Q3, AUDI Q5, AUDI Q7, BMW X1, MERCEDES E-Klasse, MERCEDES GLC-Klasse, VOLKSWAGEN Tiguan.",
  "5x112.0%66.5$20": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A6, AUDI A7, AUDI Q5, AUDI Q7, BMW X3, PORSCHE Macan.",
  "5x112.0%66.5$21": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q7, AUDI Q8, AUDI RS6, AUDI S6, PORSCHE Macan.",
  "5x112.0%66.5$22": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q8, AUDI RS Q8.",
  "5x112.0%66.5$23": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q8, AUDI SQ8.",
  "5x112.0%66.45$17": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, MERCEDES C-Klasse, SKODA Octavia, VOLKSWAGEN Tiguan.",
  "5x112.0%66.45$18": "Данный комплект дисков со сверловкой 5x112.0 подойдет на MERCEDES E-Klasse, SKODA Octavia, VOLKSWAGEN Passat, VOLKSWAGEN Teramont.",
  "5x112.0%66.45$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A4, MINI Countryman.",
  "5x112.0%66.45$20": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A6, MERCEDES GLE-Klasse, PORSCHE Macan.",
  "5x112.0%66.45$21": "Данный комплект дисков со сверловкой 5x112.0 подойдет на MERCEDES GLE-Klasse, MERCEDES GLS-Klasse, PORSCHE Macan.",
  "5x112.0%66.45$22": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q8, AUDI SQ7.",
  "5x112.0%66.5$17": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A4, MERCEDES B-Klasse, MERCEDES C-Klasse, MERCEDES SLK-Klasse, MERCEDES V-Klasse, MERCEDES Vito, SEAT Leon, SKODA Octavia, VOLKSWAGEN Jetta.",
  "5x112.0%66.5$18": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, AUDI A4, AUDI A5, AUDI A6, AUDI Q3, BMW 3-series, LEXUS RX, MERCEDES V-Klasse, SKODA Octavia, SKODA Octavia RS, SKODA Octavia Scout, SKODA Superb, VOLKSWAGEN Golf VIII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Tiguan.",
  "5x112.0%66.5$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A5, AUDI Q3, AUDI Q5, BMW 5-series, BMW X1, LAND ROVER Range Rover Sport, MERCEDES CLA-Klasse, MERCEDES CLS-Klasse, MERCEDES V-Klasse, PORSCHE Macan, SKODA Karoq, VOLKSWAGEN Passat CC, VOLKSWAGEN Tiguan.",
  "5x112.0%66.5$20": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A5, AUDI A6, AUDI A7, AUDI A8, AUDI Q7, BMW 3-series, BMW 5-series, BMW X4, MERCEDES GLC-Klasse, VOLKSWAGEN Tiguan.",
  "5x112.0%66.5$21": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A7, AUDI A8L, AUDI Q5, AUDI Q7, AUDI Q8, AUDI S8, BMW X3 M, BMW X5, MERCEDES GL-Klasse, VOLKSWAGEN Touareg.",
  "5x112.0%66.5$22": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q8, BMW X5.",
  "5x112.0%66.5$23": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q8.",
  "5x112.0%66.6$16": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A4, MERCEDES CLA-Klasse, OPEL Astra H, SKODA Octavia, SKODA Octavia RS, VOLKSWAGEN Golf VI, VOLKSWAGEN Jetta, VOLKSWAGEN Passat.",
  "5x112.0%66.6$17": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, AUDI A4, AUDI A5, AUDI A6, AUDI Q5, AUDI Q7, AUDI RS Q8, AUDI TT, BAIC S5, BMW 3-series, BMW 5-series, BMW 6-series GT, BMW X1, HONDA CR-V, KIA Ceed, LADA Vesta Sport, MERCEDES A-Klasse, MERCEDES C-Klasse, MERCEDES CLA-Klasse, MERCEDES CLC-Klasse, MERCEDES CLK-Klasse, MERCEDES CLS-Klasse, MERCEDES E-Klasse, MERCEDES GLC-Klasse, MERCEDES GLE-Klasse, MERCEDES GLK-Klasse, MERCEDES S-Klasse, MERCEDES SLK-Klasse, MERCEDES V-Klasse, MERCEDES Viano, MERCEDES Vito, MINI Clubman, MINI Countryman, MINI Coupe, MINI Hatch, OPEL Astra H, SKODA Karoq, SKODA Kodiaq, SKODA Kodiaq Scout, SKODA Octavia, SKODA Octavia RS, SKODA Superb, SKODA Yeti, SSANG YONG Actyon, VOLKSWAGEN Beetle, VOLKSWAGEN Caddy, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Golf VIII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC, VOLKSWAGEN Scirocco, VOLKSWAGEN Sharan, VOLKSWAGEN Tiguan, VOLKSWAGEN Touran.",
  "5x112.0%66.6$18": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, AUDI A4, AUDI A4 Allroad, AUDI A5, AUDI A6, AUDI A6 Allroad, AUDI A7, AUDI A8, AUDI Q3, AUDI Q5, AUDI RS Q3, AUDI TT, BMW 1-series, BMW 2-series, BMW 3-series, BMW 4-series, BMW 5-series, BMW X1, BMW X2, BMW X3, BMW X4, BMW X5 M, CHANGAN CS35 Plus, CHEVROLET Niva, HYUNDAI Veloster, LADA Niva, LADA Niva Legend, MAZDA CX-5, MERCEDES A-Klasse, MERCEDES B-Klasse, MERCEDES C-Klasse, MERCEDES CL-Klasse, MERCEDES CLA-Klasse, MERCEDES CLC-Klasse, MERCEDES CLK-Klasse, MERCEDES CLS-Klasse, MERCEDES E-Klasse, MERCEDES GL-Klasse, MERCEDES GLA-Klasse, MERCEDES GLB-Klasse, MERCEDES GLC-Klasse, MERCEDES GLE-Klasse, MERCEDES GLS-Klasse, MERCEDES M-Klasse, MERCEDES Maybach S-Klasse, MERCEDES R-Klasse, MERCEDES S-Klasse, MERCEDES SLC-Klasse, MERCEDES SLK-Klasse, MERCEDES V-Klasse, MERCEDES Vito, MERCEDES уд. ML, MINI Countryman, MINI Coupe, OPEL Astra H, SEAT Altea, SEAT Leon, SKODA Karoq, SKODA Kodiaq, SKODA Kodiaq Scout, SKODA Octavia, SKODA Octavia RS, SKODA Octavia Scout, SKODA Superb, SKODA Yeti, SSANG YONG Actyon, TOYOTA Corolla, VOLKSWAGEN Caddy, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Golf VIII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC, VOLKSWAGEN Scirocco, VOLKSWAGEN Sharan, VOLKSWAGEN Tiguan, VOLKSWAGEN Touareg.",
  "5x112.0%66.6$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на ALFA ROMEO 159, ALFA ROMEO Giulietta, AUDI A3, AUDI A4, AUDI A4 Allroad, AUDI A5, AUDI A6, AUDI A6 Allroad, AUDI A7, AUDI A8, AUDI Q3, AUDI Q5, AUDI Q7, AUDI Q8, AUDI RS Q3, AUDI S4, AUDI S5, AUDI S6, AUDI SQ5, AUDI TT, BENTLEY Continental GT, BMW 1-series, BMW 3-series, BMW 4-series, BMW 5-series, BMW 6-series GT, BMW 7-series, BMW 8-series, BMW M5, BMW X1, BMW X2, BMW X3, BMW X3 M, BMW X4, BMW X5, BMW X5 M, BMW X6, BMW X6 M, BMW X7, BMW i8, CHANGAN UNI-K, HYUNDAI Veloster, LADA Niva, LADA Niva Legend, LAND ROVER Freelander, MERCEDES A-Klasse, MERCEDES AMG GT, MERCEDES C-Klasse, MERCEDES CLA-Klasse, MERCEDES CLK-Klasse, MERCEDES CLS-Klasse, MERCEDES E-Klasse, MERCEDES GL-Klasse, MERCEDES GLA-Klasse, MERCEDES GLC-Klasse, MERCEDES GLE-Klasse, MERCEDES GLK-Klasse, MERCEDES GLS-Klasse, MERCEDES M-Klasse, MERCEDES Maybach S-Klasse, MERCEDES S-Klasse, MERCEDES SL-Klasse, MERCEDES V-Klasse, MERCEDES Viano, MERCEDES Vito, OPEL Astra H, PORSCHE Macan, SKODA Karoq, SKODA Kodiaq, SKODA Kodiaq Scout, SKODA Octavia, SKODA Superb, SSANG YONG Actyon, TOYOTA Camry, TOYOTA RAV 4, VOLKSWAGEN Arteon, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VIII, VOLKSWAGEN ID.3, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC, VOLKSWAGEN Scirocco, VOLKSWAGEN Sharan, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan.",
  "5x112.0%66.6$20": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A4, AUDI A5, AUDI A6, AUDI A6 Allroad, AUDI A7, AUDI A8, AUDI A8L, AUDI Q3, AUDI Q5, AUDI Q7, AUDI Q8, AUDI RS3, AUDI RS5, AUDI RS7, AUDI S6, AUDI e-tron, BENTLEY Continental GTC, BMW 3-series, BMW 4-series, BMW 5-series, BMW 6-series GT, BMW 7-series, BMW 8-series, BMW M5, BMW M8, BMW X1, BMW X3, BMW X3 M, BMW X4, BMW X4 M, BMW X5, BMW X5 M, BMW X6, BMW X6 M, BMW X7, BMW Z4, BMW i3, HONDA CR-V, LADA Niva, LADA Niva Legend, MERCEDES AMG GT, MERCEDES C-Klasse, MERCEDES CL-Klasse, MERCEDES CLA-Klasse, MERCEDES CLS-Klasse, MERCEDES E-Klasse, MERCEDES GL-Klasse, MERCEDES GLA-Klasse, MERCEDES GLC-Klasse, MERCEDES GLE-Klasse, MERCEDES GLK-Klasse, MERCEDES GLS-Klasse, MERCEDES M-Klasse, MERCEDES Maybach S-Klasse, MERCEDES S-Klasse, MERCEDES V-Klasse, PORSCHE Macan, SKODA Kodiaq, TOYOTA Camry, TOYOTA Supra, VOLKSWAGEN Arteon, VOLKSWAGEN Passat, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan, VOLKSWAGEN Touareg, VOLKSWAGEN Transporter.",
  "5x112.0%66.6$21": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A6, AUDI A6 Allroad, AUDI A7, AUDI A8, AUDI A8L, AUDI Q5, AUDI Q7, AUDI Q8, AUDI RS6, AUDI RS7, AUDI S8, AUDI SQ7, AUDI e-tron, BMW 3-series, BMW 5-series, BMW 7-series, BMW 8-series, BMW M5, BMW X3, BMW X3 M, BMW X4, BMW X5, BMW X5 M, BMW X6, BMW X6 M, BMW X7, BMW i8, HAVAL F7, LEXUS RX, MERCEDES AMG GT, MERCEDES C-Klasse, MERCEDES CLS-Klasse, MERCEDES E-Klasse, MERCEDES GL-Klasse, MERCEDES GLA-Klasse, MERCEDES GLC-Klasse, MERCEDES GLE-Klasse, MERCEDES GLK-Klasse, MERCEDES GLS-Klasse, MERCEDES M-Klasse, MERCEDES Maybach S-Klasse, MERCEDES S-Klasse, PORSCHE Macan, VOLKSWAGEN Tiguan, VOLKSWAGEN Touareg.",
  "5x112.0%66.6$22": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI Q7, AUDI Q8, AUDI RS Q8, AUDI SQ8, BMW 3-series, BMW 5-series, BMW 7-series, BMW X4, BMW X5, BMW X5 M, BMW X6, BMW X6 M, BMW X7, BMW i8, MERCEDES CLS-Klasse, MERCEDES GL-Klasse, MERCEDES GLC-Klasse, MERCEDES GLE-Klasse, MERCEDES GLS-Klasse, MERCEDES M-Klasse, MERCEDES Maybach GLS, MERCEDES S-Klasse, PORSCHE Macan, VOLKSWAGEN Polo, VOLKSWAGEN Touareg.",
  "5x112.0%66.6$23": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI RS Q8, BMW X5, BMW X6 M, BMW X7, MERCEDES GLE-Klasse, MERCEDES GLS-Klasse, MERCEDES Maybach GLS, ROLLS-ROYCE Cullinan.",
  "5x112.0%66.9$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на BMW 5-series.",
  "5x112.0%72.6$18": "Данный комплект дисков со сверловкой 5x112.0 подойдет на BMW 3-series, MERCEDES Vito.",
  "5x112.0%72.6$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на CHEVROLET Niva.",
  "5x112.0%73.1$17": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A3, BAIC S5, BMW X1, MERCEDES C-Klasse, MERCEDES CLA-Klasse, MERCEDES E-Klasse, SKODA Octavia, SKODA Yeti, VOLKSWAGEN Golf VI, VOLKSWAGEN Jetta, VOLKSWAGEN Passat.",
  "5x112.0%73.1$18": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A4, AUDI A5, AUDI S3, BMW 3-series, LADA Niva, MERCEDES C-Klasse, OPEL Astra H, SEAT Leon, SKODA Karoq, SKODA Kodiaq, SKODA Octavia, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat.",
  "5x112.0%73.1$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на AUDI A4, AUDI A6, AUDI Q5, BMW 5-series, Hongqi HS3, MERCEDES E-Klasse, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC.",
  "5x112.0%73.1$20": "Данный комплект дисков со сверловкой 5x112.0 подойдет на VOLKSWAGEN Touareg.",
  "5x112.0%73.1$21": "Данный комплект дисков со сверловкой 5x112.0 подойдет на VOLKSWAGEN Teramont.",
  # "5x112.0%MB$19": "Данный комплект дисков со сверловкой 5x112.0 подойдет на SKODA Octavia.",
  "5x113.0%73.1$16": "Данный комплект дисков со сверловкой 5x113.0 подойдет на BYD Yuan Pro, KIA Ceed, KIA Cerato.",
  "5x113.0%73.1$17": "Данный комплект дисков со сверловкой 5x113.0 подойдет на AUDI A3, AUDI A4, AUDI A5, AUDI A6, AUDI Q3, BMW 2-series, BMW 3-series, FAW Besturn M9, GEELY Emgrand 7, HAVAL Jolion, HAVAL M6, HONDA CR-V, HONDA Civic, HONDA Stepwgn, HONDA Stream, HYUNDAI Creta, HYUNDAI Elantra, HYUNDAI Santa Fe, HYUNDAI Sonata, HYUNDAI Tucson, INFINITI Q50, JAC J7, KIA Ceed, KIA Cerato, KIA K5, KIA Optima, KIA Sorento, KIA Soul, KIA Sportage, LADA Niva, LADA Vesta Sport, LEXUS IS, MAZDA 3, MAZDA 6, MAZDA CX-5, MERCEDES A-Klasse, MERCEDES E-Klasse, MITSUBISHI ASX, NISSAN Juke, NISSAN Qashqai, NISSAN Teana, NISSAN X-Trail, RENAULT Captur, RENAULT Duster, RENAULT Fluence, SKODA Karoq, SKODA Octavia, SKODA Octavia RS, SKODA Yeti, SUBARU Legacy, SUZUKI Vitara, TOYOTA Camry, TOYOTA Corolla, TOYOTA Crown, TOYOTA RAV 4, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Golf VIII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC, VOLKSWAGEN Tiguan.",
  "5x113.0%73.1$18": "Данный комплект дисков со сверловкой 5x113.0 подойдет на AUDI A3, AUDI A4, AUDI A5, AUDI A6, AUDI A8, AUDI Q2, AUDI Q3, AUDI Q5, AUDI Q8, AUDI TT, BELGEE X50, BMW 1-series, BMW 3-series, BMW 5-series, BMW X1, BMW X3, CHANGAN CS35 PLUS, CHANGAN UNI-V, CHEVROLET Captiva, CHEVROLET Cruze, FORD Mustang, GEELY Atlas, GEELY Coolray, GEELY Coolray (SX11), GEELY Emgrand 7, GENESIS G70, GENESIS G80, HAVAL Dargo, HAVAL H4, HAVAL H7, HAVAL Jolion, HONDA Accord, HONDA CR-V, HONDA Civic, HONDA Stepwgn, HYUNDAI Creta, HYUNDAI Elantra, HYUNDAI Palisade, HYUNDAI Santa Fe, HYUNDAI Sonata, HYUNDAI Tucson, HYUNDAI Veloster, HYUNDAI i40, Hongqi HS3, INFINITI G25, INFINITI Q50, INFINITI QX50, KIA Carnival, KIA Ceed, KIA Cerato, KIA K5, KIA K900, KIA Optima, KIA Quoris, KIA Seltos, KIA Sorento, KIA Sorento Prime, KIA Sportage, KIA Stinger, LADA Niva, LADA Niva Legend, LADA Vesta Sport, LEXUS ES, LEXUS GS, LEXUS IS, MAZDA 3, MAZDA 6, MAZDA CX-5, MERCEDES C-Klasse, MERCEDES CLA-Klasse, MERCEDES E-Klasse, MERCEDES Maybach S-Klasse, MERCEDES R-Klasse, MERCEDES S-Klasse, MINI Clubvan, MINI Coupe, MITSUBISHI ASX, MITSUBISHI Lancer, MITSUBISHI Outlander, MITSUBISHI Outlander XL, NISSAN Juke, NISSAN Murano, NISSAN Pixo, NISSAN Qashqai, NISSAN Teana, NISSAN X-Trail, RENAULT Duster, RENAULT Kaptur, SKODA Karoq, SKODA Kodiaq, SKODA Kodiaq Scout, SKODA Octavia, SKODA Octavia RS, SKODA Superb, SKODA Yeti, SUBARU Forester, SUBARU Legacy, SUZUKI Grand Vitara, TOYOTA Camry, TOYOTA Corolla, TOYOTA Crown, TOYOTA Harrier, TOYOTA Highlander, TOYOTA RAV 4, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, VOLKSWAGEN Passat, VOLKSWAGEN Passat CC, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan.",
  "5x113.0%73.1$19": "Данный комплект дисков со сверловкой 5x113.0 подойдет на AUDI A4, AUDI A5, AUDI A6, AUDI Q3, AUDI Q5, BMW 5-series, BMW X1, CHANGAN UNI-K, CHANGAN UNI-V, FORD Mustang, GEELY Coolray (SX11), GENESIS G70, GENESIS G80, HAVAL Dargo, HAVAL F7, HAVAL F7x, HAVAL Jolion, HONDA Accord, HYUNDAI Elantra, HYUNDAI Grandeur, HYUNDAI Santa Fe, Hongqi HS3, INFINITI FX35, INFINITI G25, INFINITI Q50, INFINITI QX50, KIA Carnival, KIA K5, KIA Optima, KIA Sorento, KIA Sportage, KIA Stinger, LADA Niva, LADA Niva Legend, LEXUS GS, LEXUS IS, MAZDA 6, MAZDA CX-5, MERCEDES A-Klasse, MERCEDES C-Klasse, MERCEDES CLS-Klasse, MERCEDES GLC-Klasse, NISSAN Pixo, SKODA Kodiaq, SKODA Octavia, SUBARU Legacy, TOYOTA Camry, TOYOTA RAV 4, VOLKSWAGEN Arteon, VOLKSWAGEN ID.3, VOLKSWAGEN Passat, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan.",
  "5x113.0%73.1$20": "Данный комплект дисков со сверловкой 5x113.0 подойдет на AUDI A6, AUDI A7, AUDI A8L, AUDI Q5, AUDI Q7, FORD Explorer, FORD Mustang, HAVAL F7x, HONDA CR-V, HYUNDAI Palisade, HYUNDAI Santa Fe, INFINITI FX37, INFINITI Q50, INFINITI QX70, KIA K5, KIA Sorento, LEXUS RX, MERCEDES GLC-Klasse, MERCEDES S-Klasse, TOYOTA RAV 4, VOLKSWAGEN Golf VII, VOLKSWAGEN Teramont, VOLKSWAGEN Tiguan, VOLKSWAGEN Touareg.",
  "5x114.3%54.1$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на GEELY Emgrand S.",
  "5x114.3%54.1$18": "Данный комплект дисков со сверловкой 5x114.3 подойдет на GEELY Coolray.",
  "5x114.3%56.1$19": "Данный комплект дисков со сверловкой 5x114.3 подойдет на SUBARU Forester.",
  "5x114.3%60.1$16": "Данный комплект дисков со сверловкой 5x114.3 подойдет на TOYOTA Camry, TOYOTA Corolla.",
  "5x114.3%60.1$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на LEXUS ES, LEXUS IS, TOYOTA Camry, TOYOTA Corolla, TOYOTA RAV 4.",
  "5x114.3%60.1$18": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN CS35 PLUS, GEELY Coolray, LEXUS ES, LEXUS GS, LEXUS IS, LEXUS NX, LEXUS RX, LEXUS UX, TOYOTA Alphard, TOYOTA C-HR, TOYOTA Camry, TOYOTA Corolla, TOYOTA Harrier, TOYOTA Highlander, TOYOTA RAV 4.",
  "5x114.3%60.1$19": "Данный комплект дисков со сверловкой 5x114.3 подойдет на AUDI Q8, CHANGAN CS55 Plus, CHANGAN UNI-K, CHANGAN UNI-T, GEELY Atlas Pro, GEELY Coolray, GEELY Otaka, LEXUS CT, LEXUS ES, LEXUS GS, LEXUS IS, LEXUS NX, LEXUS RX, TOYOTA Alphard, TOYOTA Camry, TOYOTA Corolla, TOYOTA Highlander, TOYOTA Mark X, TOYOTA RAV 4, TOYOTA Supra, TOYOTA Venza.",
  "5x114.3%60.1$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN CS95, CHANGAN UNI-K, CHANGAN UNI-V, LADA Niva, LEXUS ES, LEXUS NX, LEXUS RX, TOYOTA Camry, TOYOTA Crown, TOYOTA Harrier, TOYOTA Highlander, TOYOTA RAV 4.",
  "5x114.3%60.1$21": "Данный комплект дисков со сверловкой 5x114.3 подойдет на Avatr 11, CHANGAN UNI-K, FORD Explorer, LEXUS RX, TOYOTA Camry, TOYOTA Highlander, TOYOTA RAV 4.",
  "5x114.3%60.1$22": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN UNI-K.",
  "5x114.3%64.1$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HONDA CR-V.",
  "5x114.3%64.1$19": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HONDA Stepwgn.",
  "5x114.3%64.1$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HAVAL F7x, HONDA Accord.",
  "5x114.3%66.5$18": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HAVAL Dargo.",
  "5x114.3%66.1$16": "Данный комплект дисков со сверловкой 5x114.3 подойдет на RENAULT Duster, RENAULT Megane RS, TOYOTA Auris.",
  "5x114.3%66.1$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на LADA Vesta Sport, NISSAN Qashqai, NISSAN Serena, RENAULT Kaptur.",
  "5x114.3%66.1$19": "Данный комплект дисков со сверловкой 5x114.3 подойдет на LADA Vesta Sport.",
  "5x114.3%66.1$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на INFINITI QX70, NISSAN GT-R, TOYOTA RAV 4.",
  "5x114.3%66.1$21": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN UNI-K, INFINITI EX37, INFINITI M25, INFINITI QX50, INFINITI QX70, NISSAN Murano.",
  "5x114.3%66.1$22": "Данный комплект дисков со сверловкой 5x114.3 подойдет на INFINITI QX70.",
  "5x114.3%66.6$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на VOLKSWAGEN Golf VI.",
  "5x114.3%66.6$18": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HAVAL Dargo, HAVAL Jolion.",
  "5x114.3%66.6$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HAVAL F7.",
  "5x114.3%66.6$21": "Данный комплект дисков со сверловкой 5x114.3 подойдет на Wey VV7 PHEV.",
  "5x114.3%67.1$16": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HYUNDAI Creta, TOYOTA Corolla.",
  "5x114.3%67.1$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HAVAL M6, HONDA Civic, HONDA Stepwgn, HYUNDAI Tucson, HYUNDAI i40, KIA Ceed, KIA Cerato, KIA K5, LADA Niva, LADA Niva Legend, MITSUBISHI Lancer, RENAULT Kaptur, SUBARU Forester.",
  "5x114.3%67.1$18": "Данный комплект дисков со сверловкой 5x114.3 подойдет на AUDI A3, AUDI A7, GEELY Coolray, HONDA Civic, HYUNDAI Tucson, KIA Ceed, KIA Cerato, KIA K5, KIA Optima, KIA Sorento Prime, LEXUS IS, MAZDA 3, MAZDA 6, MITSUBISHI Lancer, TOYOTA C-HR, TOYOTA Crown, TOYOTA Highlander, TOYOTA RAV 4.",
  "5x114.3%67.1$19": "Данный комплект дисков со сверловкой 5x114.3 подойдет на GENESIS G80, HAVAL F7x, HONDA Accord, HONDA CR-Z, HYUNDAI Santa Fe, HYUNDAI Tucson, INFINITI G37, KIA Carnival, KIA Sorento Prime, KIA Sportage, LEXUS RX, MAZDA 6, MAZDA CX-5, MAZDA CX-9, RENAULT Koleos, TESLA Model 3, TOYOTA Camry, TOYOTA RAV 4.",
  "5x114.3%67.1$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN UNI-K, CHANGAN UNI-T, CHANGAN UNI-V, GENESIS G80, HYUNDAI Palisade, HYUNDAI Santa Fe, HYUNDAI Tucson, KIA K5, KIA Optima, KIA Sorento Prime, MASERATI Quattroporte, MAZDA CX-5, MAZDA CX-9, MITSUBISHI Outlander, TOYOTA RAV 4.",
  "5x114.3%67.1$21": "Данный комплект дисков со сверловкой 5x114.3 подойдет на MASERATI Quattroporte, MAZDA CX-9.",
  "5x114.3%67.1$22": "Данный комплект дисков со сверловкой 5x114.3 подойдет на GENESIS G80, KIA Sorento Prime, KIA Sportage.",
  "5x114.3%67.1$15": "Данный комплект дисков со сверловкой 5x114.3 подойдет на KIA Ceed.",
  "5x114.3%67.1$16": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HONDA CR-V, HYUNDAI Creta, HYUNDAI Elantra, KIA Ceed, KIA Cerato, KIA Optima, MAZDA 3, MAZDA 6, MITSUBISHI Lancer.",
  "5x114.3%67.1$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на GEELY Coolray, HAVAL Jolion, HAVAL M6, HONDA Accord, HONDA Civic, HYUNDAI Elantra, HYUNDAI i40, KIA Ceed, KIA Cerato, KIA K5, KIA Optima, KIA Seltos, KIA Sportage, LADA Niva Legend, LADA Vesta Sport, LEXUS IS, MAZDA 3, MAZDA 6, MAZDA CX-5, MITSUBISHI Lancer, NISSAN Juke, NISSAN Murano, NISSAN Qashqai, NISSAN Teana, TOYOTA Alphard, TOYOTA Camry, TOYOTA Corolla.",
  "5x114.3%67.1$18": "Данный комплект дисков со сверловкой 5x114.3 подойдет на BELGEE X50, CHANGAN CS55 Plus, CHANGAN UNI-V, GEELY Coolray, GENESIS G70, HAVAL Dargo, HAVAL F7, HAVAL H7, HAVAL Jolion, HONDA Accord, HONDA CR-V, HONDA Civic, HONDA Crosstour, HYUNDAI Elantra, HYUNDAI Palisade, HYUNDAI Santa Fe, HYUNDAI Tucson, HYUNDAI i30, HYUNDAI i40, HYUNDAI ix35, KIA Carens, KIA Ceed, KIA Cerato, KIA K5, KIA Optima, KIA Seltos, KIA Sorento, KIA Soul, KIA Sportage, LADA Niva, MAZDA 6, MAZDA CX-5, MITSUBISHI Galant, MITSUBISHI Lancer, MITSUBISHI Lancer Evolution, NISSAN Qashqai, RENAULT Kaptur, TOYOTA Camry, TOYOTA Corolla, TOYOTA RAV 4, VOLKSWAGEN Jetta.",
  "5x114.3%67.1$19": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN CS55, CHANGAN UNI-V, CHEVROLET Captiva, GENESIS G70, HAVAL F7, HONDA Accord, HONDA CR-V, HYUNDAI Santa Fe, HYUNDAI Tucson, INFINITI EX25, INFINITI G35, KIA Carnival, KIA K5, KIA Optima, KIA Sorento, KIA Sorento Prime, KIA Sportage, KIA Stinger, LEXUS GS, LEXUS RX, MAZDA 6, MAZDA CX-5, MITSUBISHI ASX, NISSAN Teana, NISSAN X-Trail, SUBARU Legacy, TOYOTA Camry, TOYOTA RAV 4.",
  "5x114.3%67.1$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN UNI-K, GEELY Coolray, GENESIS G70, GENESIS G80, HAVAL Dargo, HAVAL F7, HAVAL Jolion, HONDA Accord, HYUNDAI Palisade, HYUNDAI Santa Fe, INFINITI QX60, KIA Carnival, KIA Optima, KIA Sorento, KIA Stinger, LEXUS ES, LEXUS RX, MAZDA 6, MAZDA CX-5, MAZDA CX-9, NISSAN X-Trail, Wey VV7.",
  "5x114.3%67.1$21": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN UNI-K, GENESIS G70, HYUNDAI Palisade, HYUNDAI Santa Fe, MAZDA CX-5.",
  "5x114.3%67.1$22": "Данный комплект дисков со сверловкой 5x114.3 подойдет на GENESIS G80.",
  "5x114.3%70.5$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на FORD Explorer, FORD Mustang.",
  "5x114.3%71.6$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на DODGE Challenger.",
  "5x114.3%73.1$15": "Данный комплект дисков со сверловкой 5x114.3 подойдет на AUDI A7, HONDA Accord, LADA Niva, MAZDA 5/Premacy.",
  "5x114.3%73.1$16": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHRYSLER Grand Voyager, HONDA Accord, HONDA Civic, HONDA Stream, HYUNDAI Creta, HYUNDAI Elantra, HYUNDAI Sonata, HYUNDAI i30, KIA Ceed, KIA Ceed GT, KIA Cerato, KIA K5, KIA Optima, KIA Sorento, KIA Soul, KIA Sportage, LADA Niva, LEXUS ES, MAZDA 3, MAZDA 6, MITSUBISHI Galant, MITSUBISHI Lancer, MITSUBISHI Outlander, NISSAN Juke, NISSAN Qashqai, NISSAN Serena, RENAULT Arkana, RENAULT Duster, RENAULT Megane III, SUZUKI Grand Vitara, TOYOTA Auris, TOYOTA C-HR, TOYOTA Camry, TOYOTA Corolla, TOYOTA Crown, TOYOTA Verso, VOLKSWAGEN Golf VI.",
  "5x114.3%73.1$17": "Данный комплект дисков со сверловкой 5x114.3 подойдет на AUDI A4, BELGEE X50, CADILLAC ATS, CHANGAN UNI-V, CHEVROLET Captiva, CHEVROLET Equinox, CHEVROLET Malibu, DODGE Caliber, FAW Besturn X80, FORD Explorer, GEELY Atlas Pro, GEELY Coolray, GEELY Emgrand 7, HAVAL Dargo, HAVAL F7, HAVAL F7x, HAVAL Jolion, HAVAL M6, HONDA Accord, HONDA CR-V, HONDA Civic, HONDA Crossroad, HONDA Stepwgn, HONDA Stream, HYUNDAI Creta, HYUNDAI Elantra, HYUNDAI Grandeur, HYUNDAI Santa Fe, HYUNDAI Sonata, HYUNDAI Tucson, HYUNDAI Veloster, HYUNDAI i30, HYUNDAI i40, HYUNDAI ix35, JAC J7, KIA Carnival, KIA Ceed, KIA Ceed GT, KIA Cerato, KIA Cerato Classic, KIA K5, KIA Magentis, KIA Optima, KIA Sorento, KIA Sorento Prime, KIA Soul, KIA Sportage, KIA Stinger, LADA Niva, LADA Niva Legend, LADA Vesta Sport, LEXUS CT, LEXUS ES, LEXUS GS, LEXUS IS, LEXUS NX, LEXUS SC, MAZDA 3, MAZDA 5/Premacy, MAZDA 6, MAZDA CX-30, MAZDA CX-5, MAZDA MX-5, MITSUBISHI ASX, MITSUBISHI Galant, MITSUBISHI Lancer, MITSUBISHI Outlander, MITSUBISHI Outlander XL, NISSAN Juke, NISSAN Leaf, NISSAN Qashqai, NISSAN Serena, NISSAN Teana, NISSAN Terrano, NISSAN X-Trail, OPEL Astra J, RENAULT Arkana, RENAULT Duster, RENAULT Fluence, RENAULT Kaptur, RENAULT Laguna Grandtour III, RENAULT Laguna III, RENAULT Megane III, SUBARU Forester, SUBARU Legacy, SUZUKI Grand Vitara, SUZUKI SX4, SUZUKI Vitara, TOYOTA Alphard, TOYOTA Auris, TOYOTA C-HR, TOYOTA Camry, TOYOTA Corolla, TOYOTA RAV 4, TOYOTA Verso, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Tiguan.",
  "5x114.3%73.1$18": "Данный комплект дисков со сверловкой 5x114.3 подойдет на AUDI A5, AUDI A6, BELGEE X50, CADILLAC ATS, CHANGAN CS55, CHANGAN UNI-K, CHANGAN UNI-V, CHANGAN V7, CHEVROLET Captiva, CHEVROLET Malibu, CHEVROLET Niva, CHEVROLET Orlando, CITROEN C-Crosser, FAW Besturn B30, FAW Besturn B70, FAW Besturn B70S, FAW Besturn T55, FORD Escape, FORD Explorer, FORD Mustang, GEELY Atlas, GEELY Atlas Pro, GEELY Coolray, GEELY Coolray (SX11), GEELY Emgrand 7, GENESIS G70, GENESIS G80, HAVAL Dargo, HAVAL F7, HAVAL H2, HAVAL H4, HAVAL Jolion, HAVAL M6, HONDA Accord, HONDA CR-V, HONDA Civic, HONDA Stepwgn, HYUNDAI Creta, HYUNDAI Elantra, HYUNDAI Palisade, HYUNDAI Santa Fe, HYUNDAI Sonata, HYUNDAI Tucson, HYUNDAI Veloster, HYUNDAI i30, HYUNDAI i40, HYUNDAI ix55, INFINITI EX25, INFINITI FX30, INFINITI G25, INFINITI G35, INFINITI M35, INFINITI Q50, INFINITI Q60, INFINITI Q70, INFINITI QX50, JAC T9, KIA Carnival, KIA Ceed, KIA Ceed GT, KIA Cerato, KIA K5, KIA Optima, KIA Pro Ceed, KIA ProCeed, KIA Quoris, KIA Seltos, KIA Sorento, KIA Sorento Prime, KIA Soul, KIA Sportage, KIA Stinger, LADA Niva, LADA Niva Legend, LADA Vesta Sport, LEXUS ES, LEXUS GS, LEXUS IS, LEXUS IS F, LEXUS NX, LEXUS RX, LIFAN X60, MAZDA 3, MAZDA 5/Premacy, MAZDA 6, MAZDA CX-30, MAZDA CX-5, MERCEDES C-Klasse, MERCEDES E-Klasse, MERCEDES Viano, MITSUBISHI ASX, MITSUBISHI Eclipse, MITSUBISHI Eclipse Cross, MITSUBISHI Lancer, MITSUBISHI Lancer Evolution, MITSUBISHI Outlander, MITSUBISHI Outlander XL, NISSAN Juke, NISSAN Qashqai, NISSAN Teana, NISSAN X-Trail, OPEL Astra J, RENAULT Arkana, RENAULT Captur, RENAULT Duster, RENAULT Fluence, RENAULT Laguna III, RENAULT Megane III, RENAULT Megane RS, SUBARU Forester, SUBARU Legacy, SUBARU WRX STI, SUZUKI Grand Vitara, TESLA Model 3, TOYOTA Alphard, TOYOTA C-HR, TOYOTA Camry, TOYOTA Corolla, TOYOTA Crown, TOYOTA Harrier, TOYOTA Isis, TOYOTA Mark X, TOYOTA RAV 4, TOYOTA Supra, TOYOTA Venza, VOLKSWAGEN Golf VI, VOLKSWAGEN Golf VII, VOLKSWAGEN Jetta, Wey P8.",
  "5x114.3%73.1$19": "Данный комплект дисков со сверловкой 5x114.3 подойдет на ACURA MDX, ASTON MARTIN Vantage V8, AUDI Q5, BAW Hiace Minibus, CHANGAN CS55, CHANGAN CS55 Plus, CHANGAN UNI-K, CHANGAN UNI-T, CHANGAN UNI-V, CHEVROLET Captiva, CHEVROLET Malibu, CHEVROLET Niva, CHRYSLER 300C, CITROEN C-Crosser, Changan Auchan A600, Changan Auchan A800, FAW Hongta T340, FORD Explorer, FORD Mustang, GEELY Atlas Pro, GEELY Coolray, GEELY Coolray (SX11), GEELY Otaka, GENESIS G70, GENESIS G80, HAVAL Dargo, HAVAL F7, HAVAL F7x, HAVAL Jolion, HAVAL M6, HONDA Accord, HONDA CR-V, HONDA Civic, HYUNDAI Creta, HYUNDAI Elantra, HYUNDAI Grandeur, HYUNDAI Palisade, HYUNDAI Santa Fe, HYUNDAI Sonata, HYUNDAI Tucson, HYUNDAI Veloster, HYUNDAI i30-N, HYUNDAI ix35, Hongqi H5, INFINITI EX25, INFINITI EX35, INFINITI FX35, INFINITI G25, INFINITI G35, INFINITI G37, INFINITI M35, INFINITI Q50, INFINITI Q70, KIA Carnival, KIA Ceed, KIA Cerato, KIA K5, KIA K900, KIA Optima, KIA Quoris, KIA Sorento, KIA Sorento Prime, KIA Soul, KIA Sportage, KIA Stinger, LADA Niva, LADA Niva Legend, LEXUS ES, LEXUS GS, LEXUS IS, LEXUS IS F, LEXUS NX, LEXUS RX, LEXUS UX, MASERATI Levante, MAZDA 3, MAZDA 6, MAZDA CX-5, MAZDA CX-7, MITSUBISHI Outlander, MITSUBISHI Outlander XL, NISSAN Juke, NISSAN Qashqai, NISSAN Teana, NISSAN X-Trail, OPEL Antara, OPEL Astra J, RENAULT Arkana, RENAULT Latitude, SUBARU Legacy, TESLA Model 3, TOYOTA Alphard, TOYOTA C-HR, TOYOTA Camry, TOYOTA Corolla, TOYOTA Crown, TOYOTA Harrier, TOYOTA Highlander, TOYOTA RAV 4, TOYOTA Venza, VOLKSWAGEN Jetta.",
  "5x114.3%73.1$20": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN CS55, CHANGAN CS95, CHANGAN UNI-K, CHANGAN UNI-T, CHANGAN UNI-V, FAW Besturn B70S, FORD Escape, FORD Explorer, FORD Mustang, GEELY Coolray, GEELY Coolray (SX11), GEELY Otaka, GENESIS G70, GENESIS G80, HAVAL Dargo, HAVAL F7, HAVAL F7x, HAVAL H2, HAVAL H6, HAVAL H7, HAVAL Jolion, HONDA CR-V, HONDA Civic, HYUNDAI Palisade, HYUNDAI Santa Fe, HYUNDAI Tucson, Hongqi H6, Hongqi HS5, INFINITI EX25, INFINITI EX35, INFINITI FX35, INFINITI FX37, INFINITI Q70, INFINITI QX50, INFINITI QX60, INFINITI QX70, KIA Carnival, KIA Cerato, KIA K5, KIA Sorento, KIA Sorento Prime, KIA Sportage, KIA Stinger, LEXUS ES, LEXUS NX, LEXUS RX, MAZDA 6, MAZDA CX-30, MAZDA CX-5, MAZDA CX-9, MITSUBISHI Outlander, NISSAN Murano, NISSAN Pathfinder, NISSAN X-Trail, OPEL Antara, OPEL Astra J, RENAULT Duster, SUZUKI Grand Vitara, TESLA Model 3, TOYOTA Alphard, TOYOTA C-HR, TOYOTA Camry, TOYOTA Corolla, TOYOTA Highlander, TOYOTA RAV 4, VOLKSWAGEN Touareg.",
  "5x114.3%73.1$21": "Данный комплект дисков со сверловкой 5x114.3 подойдет на CHANGAN UNI-K, GENESIS G70, HAVAL Jolion, HYUNDAI Palisade, INFINITI FX35, INFINITI FX37, LEXUS RX, TOYOTA Highlander.",
  "5x114.3%73.1$22": "Данный комплект дисков со сверловкой 5x114.3 подойдет на HAVAL Dargo, INFINITI FX37.",
  "5x115.0%70.1$20": "Данный комплект дисков со сверловкой 5x115.0 подойдет на OPEL Astra J.",
  "5x115.0%70.3$18": "Данный комплект дисков со сверловкой 5x115.0 подойдет на CADILLAC ATS.",
  "5x115.0%71.5$20": "Данный комплект дисков со сверловкой 5x115.0 подойдет на BMW X6.",
  "5x115.0%71.5$21": "Данный комплект дисков со сверловкой 5x115.0 подойдет на DODGE Challenger.",
  "5x115.0%71.6$20": "Данный комплект дисков со сверловкой 5x115.0 подойдет на DODGE Challenger, DODGE Charger.",
  "5x120.0%59.5$18": "Данный комплект дисков со сверловкой 5x120.0 подойдет на GAC E9.",
  "5x120.0%59.5$22": "Данный комплект дисков со сверловкой 5x120.0 подойдет на GAC GS8.",
  "5x120.0%60.1$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на LEXUS LS, LEXUS TX.",
  "5x120.0%62.5$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Lixiang L7, Lixiang L9.",
  "5x120.0%62.5$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Lixiang L7, Lixiang L9, VOLKSWAGEN Touareg.",
  "5x120.0%62.5$22": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Lixiang L7, Lixiang L9.",
  "5x120.0%62.5$23": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Lixiang L7.",
  "5x120.0%63.3$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Lotus Eletra.",
  "5x120.0%63.4$22": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Lixiang L9, Polar Stone 01, ROX 1.",
  "5x120.0%64.1$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на TESLA Model X.",
  "5x120.0%64.1$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Lixiang L9.",
  "5x120.0%65.0$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на GAC GS8.",
  "5x120.0%65.1$16": "Данный комплект дисков со сверловкой 5x120.0 подойдет на VOLKSWAGEN Caravelle, VOLKSWAGEN Transporter.",
  "5x120.0%65.1$17": "Данный комплект дисков со сверловкой 5x120.0 подойдет на HONDA Pilot, VOLKSWAGEN California, VOLKSWAGEN Multivan.",
  "5x120.0%65.1$18": "Данный комплект дисков со сверловкой 5x120.0 подойдет на VOLKSWAGEN Amarok, VOLKSWAGEN Caravelle, VOLKSWAGEN Crafter, VOLKSWAGEN Multivan.",
  "5x120.0%65.1$19": "Данный комплект дисков со сверловкой 5x120.0 подойдет на VOLKSWAGEN Multivan.",
  "5x120.0%65.1$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на VOLKSWAGEN Multivan.",
  "5x120.0%66.5$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW XM.",
  "5x120.0%66.1$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Voyah Dreamer, Voyah Free.",
  "5x120.0%66.1$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на AITO M5, Voyah Free.",
  "5x120.0%66.1$22": "Данный комплект дисков со сверловкой 5x120.0 подойдет на Voyah Free.",
  "5x120.0%66.5$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW XM.",
  "5x120.0%70.5$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на CHEVROLET Camaro.",
  "5x120.0%72.6$17": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 1-series, BMW 3-series, BMW 5-series, BMW 7-series, BMW X1, BMW X3, LADA Niva, OPEL Insignia.",
  "5x120.0%72.6$18": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 1-series, BMW 2-series, BMW 3-series, BMW 3-series GT, BMW 4-series, BMW 5-series, BMW 5-series GT, BMW 6-series, BMW 7-series, BMW M2, BMW X1, BMW X3, BMW X4, BMW X5, CADILLAC CTS, GAC GS8, HONDA Legend, LADA Niva, LAND ROVER Discovery, LEXUS IS F, LEXUS LS, OPEL Insignia, VOLKSWAGEN Amarok, VOLKSWAGEN Caravelle, VOLKSWAGEN Multivan, VOLKSWAGEN Transporter.",
  "5x120.0%72.6$19": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 1-series, BMW 2-series, BMW 3-series, BMW 3-series GT, BMW 4-series, BMW 5-series, BMW 5-series GT, BMW 6-series, BMW 7-series, BMW M2, BMW M4, BMW M5, BMW M6, BMW X1, BMW X3, BMW X4, BMW X5, CADILLAC STS, CADILLAC XT4, GAC GS8, LAND ROVER Discovery, LAND ROVER Range Rover Sport, LEXUS LS, OPEL Insignia, VOLKSWAGEN Amarok, Voyah Free.",
  "5x120.0%72.6$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на ACURA MDX, ACURA TLX, BMW 1-series, BMW 3-series, BMW 3-series GT, BMW 4-series, BMW 5-series, BMW 5-series GT, BMW 6-series, BMW 7-series, BMW M6, BMW X3, BMW X4, BMW X6, BYD Song Pro, CADILLAC CTS, CHEVROLET Camaro, GAC GS8, HONDA Pilot, LAND ROVER Defender, LAND ROVER Discovery, LAND ROVER Range Rover, LAND ROVER Range Rover Sport, Lixiang L7, OPEL Insignia, VOLKSWAGEN Amarok, Voyah Dreamer, Voyah Free.",
  "5x120.0%72.6$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 6-series, BMW 7-series, CHEVROLET Camaro, LAND ROVER Discovery, LAND ROVER Freelander, LAND ROVER Range Rover, LAND ROVER Range Rover Sport, Lixiang L7, Lixiang L9, VOLKSWAGEN Touareg, Voyah Dreamer.",
  "5x120.0%72.6$22": "Данный комплект дисков со сверловкой 5x120.0 подойдет на GAC GS8, GAC GS8 Hybrid, LAND ROVER Defender, LAND ROVER Discovery, LAND ROVER Discovery Sport, LAND ROVER Range Rover, LAND ROVER Range Rover Sport, Lixiang L9.",
  "5x120.0%72.6$23": "Данный комплект дисков со сверловкой 5x120.0 подойдет на LAND ROVER Discovery Sport, LAND ROVER Range Rover, LAND ROVER Range Rover Sport.",
  "5x120.0%73.1$18": "Данный комплект дисков со сверловкой 5x120.0 подойдет на OPEL Insignia.",
  "5x120.0%73.1$19": "Данный комплект дисков со сверловкой 5x120.0 подойдет на CADILLAC CTS.",
  "5x120.0%73.1$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW X6, GAC GS8, LAND ROVER Range Rover, TOYOTA Highlander.",
  "5x120.0%74.1$17": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 1-series, BMW 3-series.",
  "5x120.0%74.1$18": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 3-series, BMW 5-series, BMW M6.",
  "5x120.0%74.1$19": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 2-series, BMW 5-series, BMW X3, BMW X5.",
  "5x120.0%74.1$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW X5, BMW X5 M, BMW X6.",
  "5x120.0%74.1$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW X5, BMW X6, LADA Niva, LAND ROVER Range Rover.",
  "5x120.0%74.1$22": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW X5.",
  "5x120.0%74.0$18": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW X5.",
  "5x120.0%74.1$18": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 3-series, BMW 5-series, MERCEDES E-Klasse, VOLKSWAGEN Amarok.",
  "5x120.0%74.1$19": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 5-series, BMW X3, BMW X5, BMW X6.",
  "5x120.0%74.1$20": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 5-series, BMW 6-series, BMW X5, BMW X5 M, BMW X6, BMW X6 M, GAC GS8, Lixiang L7, VOLKSWAGEN Touareg.",
  "5x120.0%74.1$21": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW 5-series, BMW 6-series, BMW 7-series, BMW M5, BMW X5, BMW X5 M, BMW X6, BMW X6 M, GAC GS8.",
  "5x120.0%74.1$22": "Данный комплект дисков со сверловкой 5x120.0 подойдет на BMW X5, BMW X6 M.",
  "5x127.0%71.5$17": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Grand Cherokee, JEEP Wrangler.",
  "5x127.0%71.5$18": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Grand Cherokee, JEEP Wrangler.",
  "5x127.0%71.5$19": "Данный комплект дисков со сверловкой 5x127.0 подойдет на CHRYSLER Town & Country, JEEP Grand Cherokee.",
  "5x127.0%71.5$20": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Cherokee, JEEP Grand Cherokee, JEEP Wrangler, JEEP Wrangler Unlimited.",
  "5x127.0%71.5$21": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Grand Cherokee.",
  "5x127.0%71.6$17": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Commander, JEEP Wrangler.",
  "5x127.0%71.6$18": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Grand Cherokee.",
  "5x127.0%71.6$20": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Grand Cherokee.",
  "5x127.0%77.8$18": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Wrangler.",
  "5x127.0%77.8$20": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Grand Cherokee, JEEP Wrangler.",
  "5x127.0%87.1$20": "Данный комплект дисков со сверловкой 5x127.0 подойдет на JEEP Wrangler.",
  "5x130.0%71.5$18": "Данный комплект дисков со сверловкой 5x130.0 подойдет на VOLKSWAGEN Touareg.",
  "5x130.0%71.5$19": "Данный комплект дисков со сверловкой 5x130.0 подойдет на VOLKSWAGEN Touareg.",
  "5x130.0%71.5$20": "Данный комплект дисков со сверловкой 5x130.0 подойдет на AUDI Q7, VOLKSWAGEN Touareg.",
  "5x130.0%71.5$21": "Данный комплект дисков со сверловкой 5x130.0 подойдет на PORSCHE Cayenne.",
  "5x130.0%71.5$22": "Данный комплект дисков со сверловкой 5x130.0 подойдет на BENTLEY Bentayga, PORSCHE Taycan.",
  "5x130.0%71.5$23": "Данный комплект дисков со сверловкой 5x130.0 подойдет на BENTLEY Bentayga.",
  "5x130.0%71.6$18": "Данный комплект дисков со сверловкой 5x130.0 подойдет на PORSCHE Cayman.",
  "5x130.0%71.6$19": "Данный комплект дисков со сверловкой 5x130.0 подойдет на AUDI Q7, PORSCHE Cayenne, PORSCHE Cayman.",
  "5x130.0%71.6$20": "Данный комплект дисков со сверловкой 5x130.0 подойдет на AUDI Q7, PORSCHE 911, PORSCHE Cayenne, PORSCHE Panamera, VOLKSWAGEN Touareg.",
  "5x130.0%71.6$21": "Данный комплект дисков со сверловкой 5x130.0 подойдет на AUDI Q7, BENTLEY Continental GT, LAMBORGHINI Urus, PORSCHE 911, PORSCHE Cayenne, PORSCHE Cayman, PORSCHE Panamera, PORSCHE Taycan, VOLKSWAGEN Touareg.",
  "5x130.0%71.6$22": "Данный комплект дисков со сверловкой 5x130.0 подойдет на BENTLEY Continental GT, BENTLEY Mulsanne, PORSCHE Cayenne.",
  "5x130.0%72.6$20": "Данный комплект дисков со сверловкой 5x130.0 подойдет на VOLKSWAGEN Touareg.",
  "5x130.0%84.1$16": "Данный комплект дисков со сверловкой 5x130.0 подойдет на PEUGEOT Boxer.",
  "5x130.0%84.1$19": "Данный комплект дисков со сверловкой 5x130.0 подойдет на VOLKSWAGEN Touareg.",
  "5x130.0%84.1$20": "Данный комплект дисков со сверловкой 5x130.0 подойдет на Hongqi HS7, MERCEDES G-Klasse, PORSCHE Cayenne, VOLKSWAGEN Touareg.",
  "5x130.0%84.1$21": "Данный комплект дисков со сверловкой 5x130.0 подойдет на MERCEDES G-Klasse.",
  "5x130.0%84.1$22": "Данный комплект дисков со сверловкой 5x130.0 подойдет на MERCEDES G-Klasse.",
  "5x130.0%84.1$23": "Данный комплект дисков со сверловкой 5x130.0 подойдет на MERCEDES G-Klasse.",
  "5x130.0%84.1$24": "Данный комплект дисков со сверловкой 5x130.0 подойдет на MERCEDES G-Klasse.",
  "5x139.7%108.1$15": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva.",
  "5x139.7%108.1$16": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva, LADA Niva Legend, SUZUKI Jimny, УАЗ 2360* Cargo, УАЗ 3163* Patriot, УАЗ 3909* Фермер.",
  "5x139.7%108.1$18": "Данный комплект дисков со сверловкой 5x139.7 подойдет на SUZUKI Jimny.",
  "5x139.7%108.5$15": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva Legend.",
  "5x139.7%108.5$16": "Данный комплект дисков со сверловкой 5x139.7 подойдет на SUZUKI Jimny, УАЗ 2206*, УАЗ 3163* Patriot.",
  "5x139.7%108.5$18": "Данный комплект дисков со сверловкой 5x139.7 подойдет на УАЗ 3163* Patriot.",
  "5x139.7%110.1$16": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva, LADA Niva Legend, SUZUKI Jimny, УАЗ 3163* Patriot.",
  "5x139.7%110.1$17": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva.",
  "5x139.7%110.1$18": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva, УАЗ 3163* Patriot.",
  "5x139.7%112.0$18": "Данный комплект дисков со сверловкой 5x139.7 подойдет на УАЗ 3163* Patriot.",
  "5x139.7%77.8$20": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva Legend.",
  "5x139.7%98.0$16": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva.",
  "5x139.7%98.5$16": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva.",
  "5x139.7%98.5$17": "Данный комплект дисков со сверловкой 5x139.7 подойдет на CHEVROLET Niva, LADA Niva, LADA Niva Legend.",
  "5x139.7%98.5$18": "Данный комплект дисков со сверловкой 5x139.7 подойдет на CHEVROLET Niva, LADA Niva, LADA Niva Legend.",
  "5x139.7%98.5$19": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva.",
  "5x139.7%98.5$20": "Данный комплект дисков со сверловкой 5x139.7 подойдет на LADA Niva Legend.",
  "5x150.0%100.1$20": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Land Cruiser 200.",
  "5x150.0%109.7$22": "Данный комплект дисков со сверловкой 5x150.0 подойдет на AURUS Komendant.",
  "5x150.0%110.0$17": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Tundra.",
  "5x150.0%110.0$18": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Land Cruiser 200.",
  "5x150.0%110.0$20": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200.",
  "5x150.0%110.0$21": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200.",
  "5x150.0%110.0$22": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200.",
  "5x150.0%110.0$23": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX.",
  "5x150.0%110.1$17": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Land Cruiser 200, TOYOTA Tundra.",
  "5x150.0%110.1$18": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200, TOYOTA Land Cruiser 300, TOYOTA Tundra.",
  "5x150.0%110.1$20": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200, TOYOTA Land Cruiser 300, TOYOTA Tundra.",
  "5x150.0%110.1$21": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200.",
  "5x150.0%110.1$22": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200.",
  "5x150.0%110.2$20": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX.",
  "5x150.0%110.3$17": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Land Cruiser 200.",
  "5x150.0%110.5$17": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Land Cruiser 200.",
  "5x150.0%110.5$18": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Land Cruiser 200.",
  "5x150.0%110.5$20": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX, TOYOTA Land Cruiser 200.",
  "5x150.0%110.5$22": "Данный комплект дисков со сверловкой 5x150.0 подойдет на LEXUS LX.",
  "5x150.0%112.0$18": "Данный комплект дисков со сверловкой 5x150.0 подойдет на TOYOTA Land Cruiser 200.",
  "5x160.0%65.1$15": "Данный комплект дисков со сверловкой 5x160.0 подойдет на FORD Tourneo Custom, FORD Transit.",
  "5x160.0%65.1$16": "Данный комплект дисков со сверловкой 5x160.0 подойдет на FORD Transit, FORD Transit Connect.",
  "5x160.0%65.1$18": "Данный комплект дисков со сверловкой 5x160.0 подойдет на FORD Transit.",
  "5x160.0%65.1$19": "Данный комплект дисков со сверловкой 5x160.0 подойдет на FORD Tourneo Custom.",
  "5х139.7%108.5$16": "Данный комплект дисков со сверловкой 5х139.7 подойдет на ГАЗ Соболь, УАЗ 3909* Фермер.",
  "5х139.7%110.0$16": "Данный комплект дисков со сверловкой 5х139.7 подойдет на LADA Niva.",
  "5х139.7%98.5$18": "Данный комплект дисков со сверловкой 5х139.7 подойдет на LADA Niva, LADA Niva Legend.",
  "5х150%110.0$22": "Данный комплект дисков со сверловкой 5х150 подойдет на LEXUS LX, TOYOTA Land Cruiser 200.",
  "5х150%110.1$18": "Данный комплект дисков со сверловкой 5х150 подойдет на TOYOTA Land Cruiser 200.",
  "5х150%110.1$20": "Данный комплект дисков со сверловкой 5х150 подойдет на TOYOTA Land Cruiser 200, TOYOTA Tundra.",
  "5х98%58.1$18": "Данный комплект дисков со сверловкой 5х98 подойдет на ALFA ROMEO 147.",
  "6x114.3%66.1$17": "Данный комплект дисков со сверловкой 6x114.3 подойдет на NISSAN Navara, NISSAN Pathfinder.",
  "6x114.3%66.1$18": "Данный комплект дисков со сверловкой 6x114.3 подойдет на MERCEDES X-Klasse.",
  "6x114.3%66.1$20": "Данный комплект дисков со сверловкой 6x114.3 подойдет на MERCEDES X-Klasse.",
  "6x114.3%67.1$17": "Данный комплект дисков со сверловкой 6x114.3 подойдет на NISSAN Pathfinder.",
  "6x114.3%67.1$20": "Данный комплект дисков со сверловкой 6x114.3 подойдет на KIA Mohave, NISSAN Navara.",
  "6x114.3%67.1$18": "Данный комплект дисков со сверловкой 6x114.3 подойдет на KIA Mohave.",
  "6x114.3%67.1$20": "Данный комплект дисков со сверловкой 6x114.3 подойдет на KIA Mohave.",
  "6x114.3%67.1$21": "Данный комплект дисков со сверловкой 6x114.3 подойдет на KIA Mohave.",
  "6x114.3%73.1$18": "Данный комплект дисков со сверловкой 6x114.3 подойдет на KIA Mohave, MERCEDES X-Klasse, NISSAN Navara, NISSAN Pathfinder.",
  "6x114.3%73.1$20": "Данный комплект дисков со сверловкой 6x114.3 подойдет на KIA Mohave.",
  "6x120.0%67.1$20": "Данный комплект дисков со сверловкой 6x120.0 подойдет на CADILLAC SRX.",
  "6x130.0%75.0$16": "Данный комплект дисков со сверловкой 6x130.0 подойдет на TOYOTA Hiace.",
  "6x130.0%75.0$17": "Данный комплект дисков со сверловкой 6x130.0 подойдет на TOYOTA Hiace.",
  "6x130.0%84.1$16": "Данный комплект дисков со сверловкой 6x130.0 подойдет на MERCEDES Sprinter, TOYOTA Hiace.",
  "6x130.0%84.1$17": "Данный комплект дисков со сверловкой 6x130.0 подойдет на MERCEDES Sprinter.",
  "6x135.0%110.0$20": "Данный комплект дисков со сверловкой 6x135.0 подойдет на FORD F-150.",
  "6x135.0%87.1$18": "Данный комплект дисков со сверловкой 6x135.0 подойдет на FORD F-150.",
  "6x135.0%87.1$20": "Данный комплект дисков со сверловкой 6x135.0 подойдет на FORD F-150.",
  "6x135.0/6x139.7%110.1$20": "Данный комплект дисков со сверловкой 6x135.0/6x139.7 подойдет на TOYOTA Land Cruiser Prado.",
  "6x139.7%100.1$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на MITSUBISHI Pajero, Tank 300.",
  "6x139.7%100.1$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на GREAT WALL Poer, HAVAL H5, ISUZU D-MAX, MITSUBISHI Pajero, Tank 300, Tank 500.",
  "6x139.7%100.1$19": "Данный комплект дисков со сверловкой 6x139.7 подойдет на Tank 500.",
  "6x139.7%100.1$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на BYD L3, INFINITI QX56, LEXUS LX, MITSUBISHI Pajero, TOYOTA Land Cruiser 300, Tank 300, Tank 500, Tank 500 PHEV, Tank 700.",
  "6x139.7%100.1$21": "Данный комплект дисков со сверловкой 6x139.7 подойдет на Tank 500.",
  "6x139.7%100.1$22": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, Tank 300, Tank 500, Tank 500 PHEV, Tank 700.",
  "6x139.7%106.1$16": "Данный комплект дисков со сверловкой 6x139.7 подойдет на ISUZU D-MAX, MITSUBISHI L200, Tank 300.",
  "6x139.7%106.1$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, CHANGAN Alsvin, FORD Ranger, GREAT WALL Poer, HAVAL H5, HAVAL H9, JAC T9, MITSUBISHI L200, MITSUBISHI Pajero, MITSUBISHI Pajero Sport, TOYOTA FJ Cruiser, TOYOTA Fortuner, TOYOTA Hilux pickup, TOYOTA Land Cruiser Prado, Tank 300.",
  "6x139.7%106.1$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, CHANGAN Alsvin, CHANGAN Benni, CHEVROLET Express, CHEVROLET Tahoe, CHEVROLET TrailBlazer, DODGE Ram 1500, FORD Ranger, GREAT WALL Hover H3, GREAT WALL Hover H5, GREAT WALL Poer, HAVAL H5, HAVAL H9, JAC T8, JAC T9, LEXUS GX, MITSUBISHI L200, MITSUBISHI Pajero, MITSUBISHI Pajero Sport, TOYOTA Fortuner, TOYOTA Hilux pickup, TOYOTA Land Cruiser Prado, Tank 300, Tank 400, Tank 500.",
  "6x139.7%106.1$19": "Данный комплект дисков со сверловкой 6x139.7 подойдет на HAVAL H9, TOYOTA Land Cruiser Prado, Tank 500.",
  "6x139.7%106.1$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на BYD L3, CADILLAC Escalade, CHANGAN Alsvin, CHEVROLET Tahoe, DODGE Ram 1500, GREAT WALL Hover H6, GREAT WALL Poer, HAVAL H5, JAC T8, JAC T9, LEXUS GX, MITSUBISHI L200, MITSUBISHI Pajero, MITSUBISHI Pajero Sport, NISSAN Patrol, TOYOTA Hilux pickup, TOYOTA Land Cruiser 300, TOYOTA Land Cruiser Prado, Tank 300, Tank 500.",
  "6x139.7%106.1$22": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, LEXUS GX, Tank 500.",
  "6x139.7%106.2$16": "Данный комплект дисков со сверловкой 6x139.7 подойдет на NISSAN Armada.",
  "6x139.7%106.2$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на GREAT WALL Hover H3, HYUNDAI H1/Starex, TOYOTA Hilux pickup, Tank 300.",
  "6x139.7%106.2$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CHANGAN Alsvin, CHEVROLET Tahoe, GREAT WALL Poer, TOYOTA Fortuner, TOYOTA Land Cruiser 300, TOYOTA Land Cruiser Prado.",
  "6x139.7%106.2$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на TOYOTA Hilux pickup, TOYOTA Land Cruiser Prado.",
  "6x139.7%106.3$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на Tank 300.",
  "6x139.7%108.1$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на MITSUBISHI Pajero.",
  "6x139.7%110.0$16": "Данный комплект дисков со сверловкой 6x139.7 подойдет на TOYOTA Land Cruiser Prado.",
  "6x139.7%110.0$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на DODGE Ram 1500, FOTON Tunland, GREAT WALL Poer, HAVAL H5, MITSUBISHI L200, NISSAN Patrol, TOYOTA Fortuner, TOYOTA Land Cruiser 200, TOYOTA Land Cruiser Prado, Tank 300.",
  "6x139.7%110.0$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на LADA Niva, MITSUBISHI L200, TOYOTA Land Cruiser Prado, Tank 300, Tank 500.",
  "6x139.7%110.0$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на DODGE Ram 1500, MITSUBISHI Pajero, Tank 300.",
  "6x139.7%110.1$15": "Данный комплект дисков со сверловкой 6x139.7 подойдет на TOYOTA Hiace.",
  "6x139.7%110.1$16": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CHEVROLET Express, MITSUBISHI L200, MITSUBISHI Pajero, MITSUBISHI Pajero Sport, TOYOTA Hilux pickup.",
  "6x139.7%110.1$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на BAIC BJ40, BAIC F40, FORD Ranger, MITSUBISHI L200, MITSUBISHI Pajero, MITSUBISHI Pajero Sport, NISSAN Patrol, TOYOTA Fortuner, TOYOTA Hilux pickup, TOYOTA Land Cruiser Prado, Tank 300.",
  "6x139.7%110.1$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CHANGAN Benni, CHEVROLET Tahoe, DODGE Ram 1500, FORD Ranger, GREAT WALL Poer, HAVAL H5, JAC T8, JAC T9, LEXUS GX, MITSUBISHI L200, MITSUBISHI Pajero, MITSUBISHI Pajero Sport, NISSAN Patrol, TOYOTA FJ Cruiser, TOYOTA Hilux pickup, TOYOTA Land Cruiser Prado, Tank 300, Tank 500.",
  "6x139.7%110.1$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на BAW Reach CUV, BYD L3, CHEVROLET Tahoe, DODGE Ram 1500, FORD Ranger, FOTON MPX E, GREAT WALL Poer, LEXUS GX, MITSUBISHI Pajero, NISSAN Patrol, TOYOTA Land Cruiser Prado, Tank 300, Tank 500, Tank 700.",
  "6x139.7%110.5$16": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CHEVROLET Avalanche, MITSUBISHI L200, NISSAN Patrol.",
  "6x139.7%110.5$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на BAIC BJ40, MITSUBISHI Pajero Sport, Tank 300.",
  "6x139.7%110.5$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на GREAT WALL Poer, Tank 300.",
  "6x139.7%110.5$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на TOYOTA 4Runner.",
  "6x139.7%112.0$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на MITSUBISHI Pajero.",
  "6x139.7%112.0$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на MITSUBISHI Pajero.",
  "6x139.7%67.1$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на MITSUBISHI Pajero Sport.",
  "6x139.7%77.8$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на DODGE Ram 1500.",
  "6x139.7%77.8$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CHEVROLET Tahoe, DODGE Ram 1500, DODGE Ram 3500, INFINITI QX56.",
  "6x139.7%77.8$22": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, DODGE Ram 1500, INFINITI QX80.",
  "6x139.7%78.1$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, CHEVROLET Tahoe, INFINITI QX56, INFINITI QX80, MITSUBISHI Pajero.",
  "6x139.7%78.1$21": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CHEVROLET Tahoe.",
  "6x139.7%78.1$22": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, CHEVROLET Tahoe, INFINITI QX80, TOYOTA Land Cruiser Prado.",
  "6x139.7%78.1$24": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade.",
  "6x139.7%92.5$17": "Данный комплект дисков со сверловкой 6x139.7 подойдет на HYUNDAI H1/Starex.",
  "6x139.7%92.5$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на FORD Ranger, HYUNDAI Grand Santa Fe, HYUNDAI Staria.",
  "6x139.7%92.5$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на HYUNDAI Staria.",
  "6x139.7%95.1$18": "Данный комплект дисков со сверловкой 6x139.7 подойдет на FORD Ranger, HAVAL H9, HYUNDAI Staria, LEXUS LX, MITSUBISHI Pajero, TOYOTA Land Cruiser 300, TOYOTA Land Cruiser Prado.",
  "6x139.7%95.1$20": "Данный комплект дисков со сверловкой 6x139.7 подойдет на LEXUS LX, TOYOTA Land Cruiser 300, TOYOTA Land Cruiser Prado, TOYOTA Sequoia.",
  "6x139.7%95.1$21": "Данный комплект дисков со сверловкой 6x139.7 подойдет на TOYOTA Land Cruiser 300.",
  "6x139.7%95.1$22": "Данный комплект дисков со сверловкой 6x139.7 подойдет на CADILLAC Escalade, LEXUS GX, LEXUS LX, TOYOTA Land Cruiser 300, TOYOTA Land Cruiser Prado, TOYOTA Sequoia.",
  "6x170.0%130.0$16": "Данный комплект дисков со сверловкой 6x170.0 подойдет на ГАЗ Газель, ГАЗ Газель Next.",
  "8x100.0/108.0%63.4$16": "Данный комплект дисков со сверловкой 8x100.0/108.0 подойдет на FORD Fiesta.",
  "8x100.0/108.0%67.1$16": "Данный комплект дисков со сверловкой 8x100.0/108.0 подойдет на LADA Granta, LADA Vesta.",
  "8x100.0/108.0%73.1$15": "Данный комплект дисков со сверловкой 8x100.0/108.0 подойдет на FORD Fiesta, FORD Fusion, HYUNDAI Solaris, KIA Rio, LADA Granta, LADA Priora, MAZDA 2/Demio, PEUGEOT 207.",
  "8x100.0/108.0%73.1$16": "Данный комплект дисков со сверловкой 8x100.0/108.0 подойдет на CHEVROLET Spark, CITROEN C4, DATSUN Mi-Do, DATSUN On-Do, FORD Ecosport, FORD Fusion, HYUNDAI Solaris, KIA Rio, KIA Rio X-Line, KIA Spectra, LADA Granta, LADA Kalina, LADA Priora, LADA Vesta, LADA X-Ray, NISSAN Almera Classic, NISSAN Micra/March, NISSAN Note, PEUGEOT 308, RENAULT Logan, SUZUKI Swift.",
  "8x100.0/108.0%73.1$17": "Данный комплект дисков со сверловкой 8x100.0/108.0 подойдет на FORD Ecosport, FORD Fiesta, FORD Fusion, HYUNDAI Solaris, KIA Rio, LADA Granta, LADA Kalina, LADA Largus, LADA Priora, LADA Samara, LADA Vesta, MINI Hatch, PEUGEOT 208, PEUGEOT 308, PEUGEOT 408, PEUGEOT Partner, RENAULT Logan, RENAULT Megane II.",
  "8x100.0/114.3%67.1$16": "Данный комплект дисков со сверловкой 8x100.0/114.3 подойдет на LADA X-Ray.",
  "8x100.0/114.3%73.1$14": "Данный комплект дисков со сверловкой 8x100.0/114.3 подойдет на CHEVROLET Lacetti, DAEWOO Matiz, DAIHATSU Terios, HONDA Fit Shuttle, HYUNDAI Getz, KIA Picanto, KIA Rio, KIA Spectra, LADA Granta, LADA Priora.",
  "8x100.0/114.3%73.1$15": "Данный комплект дисков со сверловкой 8x100.0/114.3 подойдет на CHEVROLET Aveo, CHEVROLET Lacetti, DAEWOO Gentra, DAEWOO Matiz, HONDA Fit, HYUNDAI Accent Tagaz, HYUNDAI Solaris, KIA Picanto, KIA Rio, LADA Granta, LADA Priora, LADA Vesta, MAZDA 2/Demio, NISSAN Almera Classic, NISSAN NP300, NISSAN Tiida, RENAULT Sandero, TOYOTA bB.",
  "8x100.0/114.3%73.1$16": "Данный комплект дисков со сверловкой 8x100.0/114.3 подойдет на CHEVROLET Aveo, CHEVROLET Cobalt, CHEVROLET Epica, CHEVROLET Lacetti, CITROEN C4, DAEWOO Gentra, HONDA Fit, HONDA Fit Shuttle, HONDA Freed/Freed Spike, HYUNDAI Getz, HYUNDAI Solaris, HYUNDAI Sonata, KIA Rio, KIA Rio X, KIA Rio X-Line, KIA Spectra, LADA Granta, LADA Kalina, LADA Largus, LADA Priora, LADA Vesta, LADA X-Ray, MITSUBISHI Galant, NISSAN Almera Classic, NISSAN Cube, NISSAN Micra/March, NISSAN Note, NISSAN Tiida, OPEL Corsa D, RENAULT Logan, RENAULT Sandero, RENAULT Sandero Stepway, TOYOTA Corolla Fielder, TOYOTA Succeed/Probox, TOYOTA bB.",
  "8x100.0/114.3%73.1$17": "Данный комплект дисков со сверловкой 8x100.0/114.3 подойдет на CHEVROLET Epica, CHEVROLET Lacetti, DAEWOO Gentra, FORD Fusion, HYUNDAI Solaris, HYUNDAI Sonata, KIA Rio, KIA Rio X, KIA Spectra, LADA Granta, LADA Largus, LADA Priora, LADA Vesta, LADA X-Ray, MINI Hatch, MITSUBISHI Galant, NISSAN Almera, NISSAN Almera Classic, NISSAN Note, NISSAN Tiida.",
  "8x100.0/114.3%73.1$18": "Данный комплект дисков со сверловкой 8x100.0/114.3 подойдет на CHEVROLET Epica, HYUNDAI Solaris, KIA Rio, LADA Priora, LADA Vesta.",
  "8x165.1%116.7$24": "Данный комплект дисков со сверловкой 8x165.1 подойдет на HUMMER EV, HUMMER H3T.",
  "8x98.0/100.0%73.1$14": "Данный комплект дисков со сверловкой 8x98.0/100.0 подойдет на LADA Kalina, LADA Priora.",
  "8x98.0/100.0%73.1$15": "Данный комплект дисков со сверловкой 8x98.0/100.0 подойдет на KIA Rio, LADA Granta, LADA Priora.",
  "8x98.0/100.0%73.1$16": "Данный комплект дисков со сверловкой 8x98.0/100.0 подойдет на HONDA Fit, HYUNDAI Solaris, KIA Rio, KIA Spectra, LADA Granta, LADA Priora, LADA Vesta.",
  "8x98.0/100.0%73.1$17": "Данный комплект дисков со сверловкой 8x98.0/100.0 подойдет на HYUNDAI Solaris, KIA Rio, LADA Granta.",
  "8x98.0/114.3%73.1$15": "Данный комплект дисков со сверловкой 8x98.0/114.3 подойдет на LADA Priora.",
  "8x98.0/114.3%73.1$16": "Данный комплект дисков со сверловкой 8x98.0/114.3 подойдет на LADA Priora."
}




def shuffle_text(text):
    lines = text.strip().split('\n')
    first_line = lines[0]
    other_lines = lines[1:]
    random.shuffle(other_lines)
    
    shuffled_text = first_line + '\n' + '\n'.join(other_lines)
    
    return shuffled_text

ADVANT_TEXT_RIMS = """Преимущество работы с Rimzоnа:
<strong>▪️ 3d ВИЗУАЛИЗАЦИЯ ДИСКОВ НА ВАШЕ АВТО(см.2 фото)</strong>
▪️ Если вы из другого города, то ОПЛАТИТЬ диски можно ПРИ ПОЛУЧЕНИИ (наложенный платеж).
▪️ Любой способ оплаты (оплата КРЕДИТНОЙ картой, на расчетный счёт, в том числе с НДС)
▪️ Доукомплектуем шинами, датчиками, бережно установим и заберем ваши колеса на хранение.
▪️ Сделаем примерку на ваш автомобиль.
▪️ Знаем про нестандартные диски всё.
▪️ Самый большой ассортимент стильных дисков на любое авто.
▪️ Цена указанa за oдин диск. Продаем тoлько кoмплектoм."""

ADVANT_TEXT_TIRES = """Преимуществa:
▪️ Вoзмoжнa пoкупкa с НДС
▪️ Различные брeнды и пapамeтpы шин в нaличии и под зaказ
▪️ Дoукомплeктуeм диcкaми, дaтчикaми и бepeжнo устaнoвим
▪️ При пoкупкe нe толькo шин, но и диcков, сделаeм oнлайн примерку на вaш aвтомoбиль
▪️ Доcтaвкa по всей Рoссии транспортными компаниями Деловые Линии, ПЭК, Энергия, КИТ"""

def generate_rims_card_specs(card):
    colors = {
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
    if not card:
        return ''
    
    keys = {
        'model': "Модель - {}",
        'diameter': "Диаметр диска - {}",
        'width': "Ширина диска - {}",  
        'et': "Вылет дисков - {}",     
        'bolts': "Сверловка, PCD - {}x{}",  
        'dia': "ЦО, DIA - {}",  
    }

    color_value = colors[card['color']] if card['color'] in colors else "соответствует фото"

    static_lines = [
        f"Цвет - {color_value}",
        "Упаковка - заводская коробка",
        "Заглушки на ЦО идут в ПОДАРОК"
    ]

    description_lines = []

    for key, template in keys.items():
        if key in card:
            if key == 'bolts':
                bolts = card.get('bolts', '')
                pcd = card.get('pcd', '')
                bolts2 = card.get('bolts2', '')
                pcd2 = card.get('pcd2', '')
                line = None
                if bolts2 and pcd2:
                    line = f"Сверловка, PCD - {bolts}x{pcd}/{bolts2}x{pcd2}"
                elif bolts and pcd:
                    line = f"Сверловка, PCD - {bolts}x{pcd}"
                if line:
                    description_lines.append(line)
            elif key == 'width':
                width = card.get('width', '')
                width2 = card.get('width2', '')
                if width2:
                    line = template.format(f"{width}/{width2}")
                else:
                    line = template.format(width)
                description_lines.append(line)
            elif key == 'et':
                et = card.get('et', '')
                et2 = card.get('et2', '')
                if et2:
                    line = template.format(f"{et}/{et2}")
                else:
                    line = template.format(et)
                description_lines.append(line)
            elif key == 'dia':
                dia = card.get('dia', '')
                dia2 = card.get('dia2', '')
                if dia2:
                    line = template.format(f"{dia}/{dia2}")
                else:
                    line = template.format(dia)
                description_lines.append(line)
            else:
                description_lines.append(template.format(card[key]))

    description_lines.extend(static_lines)

    description = "\n".join(description_lines)
    return description

def generate_tires_card_specs(card):

    if not card:
        return ''
    description = f"""
Характеристика шин:
Размер: {card['TireSectionWidth']}/{card['TireAspectRatio']} R{card['RimDiameter']}
Сезон: лето
Состояние: новое
Индекс скорости: {card['LoadIndex']}{card['SpeedIndex']} 
Производитель: {card['Brand']} {card['Model']}
"""

    return description


def format_alloy_rim_desc(card: dict, sv: bool=False):
    """returns a formatted string with alloy rim description.

    :param card: a product card.
    :param sv: is the product in the 1С database.
    :return: a string.
    """
    pcd_text = PCD_DICT.get(f"{card.get('bolts', '')}x{float(card.get('pcd', 0))}%{float(card.get('dia', 0))}${card.get('diameter', '')}", '')
    title = card['feed_title'] if 'feed_title' in card else ''
    


    desc = f'''{title}.

Огромный ассортимент литых дисков в наличии!

Ищете качественные литые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект литых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!

{pcd_text}

Чёрная пятница - скидки до 25% на определённые модели дисков! Большое количество различных моделей в наличии со скидкой, успей приобрести только до 30 ноября!

Почему выбирают Default?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные литые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. — оплачивайте при получении.
* 💳 Гибкие способы оплаты: наличные, карта, Сплит, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам литых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по литым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных литых дисков до эксклюзивных моделей, включая литые диски на зиму.
* ⭐️ Отзывы на литые диски в Default подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

О компании Default
Default — это надежный поставщик литых и кованых дисков с 2015 года.
Мы работаем напрямую с заводами-производителями, благодаря чему предлагаем диски оптом и в розницу по лучшим условиям.
Купить литые диски с доставкой по России — просто: выберите модель, укажите параметры и получите комплект в кратчайшие сроки.
В каталоге:
✔️ литые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать литые диски,
* узнать цены и наличие,
* получить советы по выбору литых дисков,
* или просто купить диски недорого в вашем городе.

🎯 Спешите! 
Количество комплектов ограничено. Успейте купить литые диски со скидкой, пока ещё есть в наличии!'''

    return desc





def format_alloy_rim_desc_by_diameter(card: dict, sv: bool=False):
    """returns a formatted string with alloy rim description.

    :param card: a product card.
    :param sv: is the product in the 1С database.
    :return: a string.
    """
    pcd_text = PCD_DICT.get(f"{card.get('bolts', '')}x{float(card.get('pcd', 0))}%{float(card.get('dia', 0))}${card.get('diameter', '')}", '')
    title = card['feed_title'] if 'feed_title' in card else ''
    


    desc = f'''{title}.

Огромный ассортимент литых дисков в наличии!

Ищете качественные литые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект литых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!

{pcd_text}

Чёрная пятница - скидки до 25% на определённые модели дисков! Большое количество различных моделей в наличии со скидкой, успей приобрести только до 30 ноября!

Почему выбирают Default?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные литые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. — оплачивайте при получении.
* 💳 Гибкие способы оплаты: наличные, карта, Сплит, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам литых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по литым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных литых дисков до эксклюзивных моделей, включая литые диски на зиму.
* ⭐️ Отзывы на литые диски в Default подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

О компании Default
Default — это надежный поставщик литых и кованых дисков с 2015 года.
Мы работаем напрямую с заводами-производителями, благодаря чему предлагаем диски оптом и в розницу по лучшим условиям.
Купить литые диски с доставкой по России — просто: выберите модель, укажите параметры и получите комплект в кратчайшие сроки.
В каталоге:
✔️ литые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать литые диски,
* узнать цены и наличие,
* получить советы по выбору литых дисков,
* или просто купить диски недорого в вашем городе.

🎯 Спешите! 
Количество комплектов ограничено. Успейте купить литые диски со скидкой, пока ещё есть в наличии!'''

    return desc

def format_alloy_rim_desc_by_city_and_diameter(title: str, city: str, pcd='', specs=None):
    """returns a formatted string with the alloy rim description for
    offline showrooms.

    :param title: a string with the rim title from database.
    :param city: a string with name of xml file.
    :param pcd: a string with rim pcd.
    :return: a string.
    """
    if specs is None:
        specs = ""
    else:
        specs = f"\n{specs}\n"
    work_time = '''📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.
г. Самара, ул. Дыбенко, 95к1
г. Москва,  ул. Ташкентская 28 строение 1
'''
    if city == 'avito_kzn.xml':
        work_time = "📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"
    elif city == 'avito_smr.xml':
        work_time = "📍НАШ АДРЕС: г. Самара, ул. Дыбенко, 95к1"
    elif city == 'avito_msk.xml':
        work_time = "📍НАШ АДРЕС: г. Москва, ул. Ташкентская 28 строение 1\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"
    pcd_text = ''
    if pcd != '':
        pcd_text = PCD_DICT.get(pcd, '')
        

    desc = f'''{title}.

Огромный ассортимент литых дисков в наличии!

Ищете качественные литые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект литых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!

{pcd_text}

Чёрная пятница - скидки до 25% на определённые модели дисков! Большое количество различных моделей в наличии со скидкой, успей приобрести только до 30 ноября!

Почему выбирают Default?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные литые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. — оплачивайте при получении.
* 💳 Гибкие способы оплаты: наличные, карта, Сплит, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам литых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по литым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных литых дисков до эксклюзивных моделей, включая литые диски на зиму.
* ⭐️ Отзывы на литые диски в Default подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

О компании Default
Default — это надежный поставщик литых и кованых дисков с 2015 года.
Мы работаем напрямую с заводами-производителями, благодаря чему предлагаем диски оптом и в розницу по лучшим условиям.
Купить литые диски с доставкой по России — просто: выберите модель, укажите параметры и получите комплект в кратчайшие сроки.
В каталоге:
✔️ литые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

{work_time}

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать литые диски,
* узнать цены и наличие,
* получить советы по выбору литых дисков,
* или просто купить диски недорого в вашем городе.

🎯 Спешите! 
Количество комплектов ограничено. Успейте купить литые диски со скидкой, пока ещё есть в наличии!
'''
    return desc


def format_forged_rim_desc(card: dict, sv: bool=False):
    """returns a formatted string with forged rim description.

    :param card: a product card.
    :param sv: is the product in the 1С database.
    :return: a string.
    """

    pcd_text = PCD_DICT.get(f"{card.get('bolts', '')}x{float(card.get('pcd', 0))}%{float(card.get('dia', 0))}${card.get('diameter', '')}", '')
    title = card['feed_title'] if 'feed_title' in card else ''
    


    desc = f'''{title}.
    
Огромный ассортимент кованых дисков в наличии!

Ищете качественные кованые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект кованых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!
📉 Сезонная скидка – до 25000 рублей на кованые диски! В продаже — кованые диски 16, 17, 18, 19, 20, 21, 22, 23 и 24  радиуса  — много комплектов в наличии!

{pcd_text}

Наша компания предлагает кованые диски недорого, в том числе брендовые, оригинальные и даже премиум модели.
Мы предлагаем не только кованые диски в наличии, так же большое количество кованых дисков можем изготовить на заказ по индивидуальному дизайну, диски комплектом (4 штуки) с возможностью заказать болты и датчики давления.
Изготовим любые кованые диски – даже самые смелые идеи!

Почему выбирают Default?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные кованые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. 
* 💳 Гибкие способы оплаты: наличные, карта, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам кованых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по кованым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных кованых дисков до эксклюзивных моделей, включая кованые диски на зиму.
* ⭐️ Отзывы на кованые диски в Default подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

О компании Default
Default — это надежный поставщик литых и кованых дисков с 2015 года.
Мы работаем напрямую с заводами-производителями, благодаря чему предлагаем диски оптом и в розницу по лучшим условиям.
Купить кованые диски с доставкой по России — просто: выберите модель, укажите параметры и получите комплект в кратчайшие сроки.
В каталоге:
✔️ кованые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать литые и кованые диски,
* узнать цены и наличие,
* получить советы по выбору кованых дисков,
* или просто купить диски недорого в вашем городе.

🎯 Спешите! 
Количество комплектов ограничено. Успейте купить кованые диски со скидкой, пока ещё есть в наличии!
'''



    return desc


def format_tire_desc(card: dict):
    """returns a formatted string description for tires.

    :param card: a tire card.
    :return: a string.
    """
    desc = f'''{card["Title"]}. Цена указана за одну шину.

{shuffle_text(ADVANT_TEXT_TIRES)}
{generate_tires_card_specs(card)}
Способы оплаты: оплата производится Ндс/расчётный счет/наличными/по терминалу.

Сеть магазинов Римзона – профессионально подбираем колеса с 2015г. Сотрудничаем с крупными заводами КНР по литым и кованым дискам. Лучшее соотношение цены/качества.

Звоните или пишите, что бы заказать диски или получить консультацию! С полным перечнем товаров можно ознакомиться в самом магазине Римзона.'''
    return desc



def format_spring_desc(title: str):
    """returns a formatted string with spring description.

    :param title: a string with the rim title from database.
    :return: a string.
    """
    desc = f'''
<p>{title}. Цена указана за комплект – 4 штуки.<br /> <br /> <strong>Преимущества</strong>:<br /> ▪ Уменьшенный клиренс<br /> ▪ Улучшении управляемости<br /> ▪ Устойчивость на дороге<br /> <br /> <strong>❗Звони прямо сейчас</strong> и мы поможем с выбором.<br /> На связи каждый день<strong> </strong>с 09.00 до 20:00 по МСК времени.<br /> <br /> 🚚 <strong>Доставка</strong> по России транспортными компаниями Деловые Линии, ПЭК, Энергия, КИТ.<br /> <br /> <em>❗Звоните или пишите, что бы заказать диски или получить консультацию! С полным перечнем товаров можно ознакомиться в самом магазине Римзона.</em></p>'''
    return desc


def format_alloy_rim_desc_by_city(title: str, city: str, pcd='', specs=None):
    """returns a formatted string with the alloy rim description for
    offline showrooms.

    :param title: a string with the rim title from database.
    :param city: a string with name of xml file.
    :param pcd: a string with rim pcd.
    :param specs: a string with rims specs, default is None
    :return: a string.
    """
    if specs is None:
        specs = ""
    else:
        specs = f"\n{specs}\n"
    work_time = '''📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.
г. Самара, ул. Дыбенко, 95к1
г. Москва,  ул. Ташкентская 28 строение 1
'''
    if city == 'avito_kzn.xml':
        work_time = "📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"
    elif city == 'avito_smr.xml':
        work_time = "📍НАШ АДРЕС: г. Самара, ул. Дыбенко, 95к1"
    elif city == 'avito_msk.xml':
        work_time = "📍НАШ АДРЕС: г. Москва, ул. Ташкентская 28 строение 1\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"
    pcd_text = ''
    if pcd != '':
        pcd_text = PCD_DICT.get(pcd, '')



    desc = f'''{title}.

Огромный ассортимент литых дисков в наличии!

Ищете качественные литые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект литых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!

{pcd_text}

Чёрная пятница - скидки до 25% на определённые модели дисков! Большое количество различных моделей в наличии со скидкой, успей приобрести только до 30 ноября!

Почему выбирают Default?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные литые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. — оплачивайте при получении.
* 💳 Гибкие способы оплаты: наличные, карта, Сплит, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам литых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по литым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных литых дисков до эксклюзивных моделей, включая литые диски на зиму.
* ⭐️ Отзывы на литые диски в Default подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

О компании Default
Default — это надежный поставщик литых и кованых дисков с 2015 года.
Мы работаем напрямую с заводами-производителями, благодаря чему предлагаем диски оптом и в розницу по лучшим условиям.
Купить литые диски с доставкой по России — просто: выберите модель, укажите параметры и получите комплект в кратчайшие сроки.
В каталоге:
✔️ литые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

{work_time}

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать литые диски,
* узнать цены и наличие,
* получить советы по выбору литых дисков,
* или просто купить диски недорого в вашем городе.

🎯 Спешите! 
Количество комплектов ограничено. Успейте купить литые диски со скидкой, пока ещё есть в наличии!
'''

    return desc

def format_forged_rim_desc_by_city(title: str, city: str, pcd='', specs=None):
    """returns a formatted string with the forged rim description for
        offline showrooms.

    :param title: a string with the rim title from database.
    :param city: a string with name of xml file.
    :param pcd: a string with rim pcd.
    :param specs: a string with rims specs, default is None
    :return: a string.
    """
    if specs is None:
        specs = ""
    else:
        specs = f"\n{specs}\n"
    work_time = '''📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.
г. Самара, ул. Дыбенко, 95к1
г. Москва,  ул. Ташкентская 28 строение 1
'''
    if city == 'avito_kzn.xml':
        work_time = "📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"
    elif city == 'avito_smr.xml':
        work_time = "📍НАШ АДРЕС: г. Самара, ул. Дыбенко, 95к1"
    elif city == 'avito_msk.xml':
        work_time = "📍НАШ АДРЕС: г. Москва, ул. Ташкентская 28 строение 1\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"
    
    pcd_text = ''
    if pcd != '':
        pcd_text = PCD_DICT.get(pcd, '')


    desc = f'''{title}.
    
Огромный ассортимент кованых дисков в наличии!

Ищете качественные кованые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект кованых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!
📉 Сезонная скидка – до 25000 рублей на кованые диски! В продаже — кованые диски 16, 17, 18, 19, 20, 21, 22, 23 и 24  радиуса  — много комплектов в наличии!

{pcd_text}

Наша компания предлагает кованые диски недорого, в том числе брендовые, оригинальные и даже премиум модели.
Мы предлагаем не только кованые диски в наличии, так же большое количество кованых дисков можем изготовить на заказ по индивидуальному дизайну, диски комплектом (4 штуки) с возможностью заказать болты и датчики давления.
Изготовим любые кованые диски – даже самые смелые идеи!

Почему выбирают Default?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные кованые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. 
* 💳 Гибкие способы оплаты: наличные, карта, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам кованых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по кованым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных кованых дисков до эксклюзивных моделей, включая кованые диски на зиму.
* ⭐️ Отзывы на кованые диски в Default подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

О компании Default
Default — это надежный поставщик литых и кованых дисков с 2015 года.
Мы работаем напрямую с заводами-производителями, благодаря чему предлагаем диски оптом и в розницу по лучшим условиям.
Купить кованые диски с доставкой по России — просто: выберите модель, укажите параметры и получите комплект в кратчайшие сроки.
В каталоге:
✔️ кованые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

{work_time}

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать литые и кованые диски,
* узнать цены и наличие,
* получить советы по выбору кованых дисков,
* или просто купить диски недорого в вашем городе.

🎯 Спешите! 
Количество комплектов ограничено. Успейте купить кованые диски со скидкой, пока ещё есть в наличии!
'''

    return desc

def format_tire_desc_by_city(city: str, card: dict):
    """returns a formatted string with tire description for the
        offline showrooms.

    :param city: a string with name of xml file.
    :param card: a tire card.
    :return: a string.
    """
    
    work_time = '''📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.
г. Самара, ул. Дыбенко, 95к1
г. Москва,  ул. Ташкентская 28 строение 1
'''
    if city == 'avito_kzn.xml':
        work_time = "📍НАШ АДРЕС: г. Казань ул. Спартаковская 12. Работаем с 9.00-20.00.\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"
    elif city == 'avito_smr.xml':
        work_time = "📍НАШ АДРЕС: г. Самара, ул. Дыбенко, 95к1"
    elif city == 'avito_msk.xml':
        work_time = "📍НАШ АДРЕС: г. Москва, ул. Ташкентская 28 строение 1\n🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков"

    desc = f'''
{card["Title"]}. <strong>Цена указана за одну шину.</strong>

{shuffle_text(ADVANT_TEXT_TIRES)}
{generate_tires_card_specs(card)}
{work_time}

<strong>Оплата производится Ндс/расчётный счет/наличными/по терминалу.</strong>

Остались вопросы? <strong>На связи каждый день с 09.00 до 20:00 по МСК времени.</strong>

❗️Цены и остатки могут меняться, уточняйте у наших специалистов. С полным перечнем товаров можно ознакомиться в самом магазине Rimzоnа.'''

    return desc


def format_alloy_rim_desc_by_city_msk_piter_new(title: str, city: str, pcd='', dor=0):
    """returns a formatted string with the alloy rim description for
    offline showrooms.

    :param title: a string with the rim title from database.
    :param city: a string with name of xml file.
    :param pcd: a string with rim pcd.
    :return: a string.
    """
    city_text = ''
    if city == 'avito_msk_new.xml':
        city_text = "🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков\n"
    
    pcd_text = ''
    if pcd != '':
        pcd_text = PCD_DICT.get(pcd, '')

    if dor == 0:
        price_text = '▪️Цена указан за один диск;'
    else:
        price_text = ''


    desc = f'''{title}.

В НАЛИЧИИ! Огромный ассортимент дисков на любой автомобиль!

Ищете качественные литые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект литых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!
📉 Сезонная ликвидация – скидки до 25% на избранные модели! В продаже — литые диски 15, 16, 17, 18, 19, 20, 21, 22 и 23  радиуса  — всё в наличии.
Также доступна покупка в рассрочку через Сплит — выбирайте удобный способ оплаты.

{pcd_text}

Наша компания предлагает литые диски недорого, в том числе брендовые, оригинальные и даже премиум модели.
Мы предлагаем не только литые диски в наличии, так же большое количество кованых дисков в наличии, диски комплектом (4 штуки) с возможностью заказать болты и датчики давления.
Литые диски 5×114,3, 5×112, 4×100, et35, et40, et45, DIA 67.1, 72.6 — у нас есть всё.

Почему выбирают наш магазин дисков?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные литые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. — оплачивайте при получении.
* 💳 Гибкие способы оплаты: наличные, карта, Сплит, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам литых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по литым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных литых дисков до эксклюзивных моделей, включая литые диски на зиму.
* ⭐️ Отзывы на литые диски подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

✔️ литые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать литые диски,
* узнать цены и наличие,
* получить советы по выбору литых дисков,
* или просто купить диски недорого в вашем городе.

🎯 Спешите! 
Количество комплектов ограничено. Успейте купить литые диски со скидкой, пока ещё есть в наличии!
'''

    return desc

def format_forged_rim_desc_by_city_msk_piter_new(title: str, city: str, pcd=''):
    """returns a formatted string with the forged rim description for
        offline showrooms.

    :param title: a string with the rim title from database.
    :param city: a string with name of xml file.
    :param pcd: a string with rim pcd.
    :return: a string.
    """
    
    pcd_text = ''
    if pcd != '':
        pcd_text = PCD_DICT.get(pcd, '')

    city_text = ''
    if city == 'avito_msk_new.xml':
        city_text = "🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков\n"
    

    desc = f'''{title}.
    
В НАЛИЧИИ! Огромный ассортимент кованых литых дисков на любой автомобиль! 

Ищете качественные кованые диски? Напишите «Хочу каталог, укажите марку и год авто», и мы подберем идеальный комплект кованых дисков специально для вашего автомобиля!
Заводская гарантия, бесплатная примерка и быстрая доставка по всей России – ваш комфорт и спокойствие гарантированы!

{pcd_text}

Наша компания предлагает кованые диски недорого, в том числе брендовые, оригинальные и даже премиум модели.
Мы предлагаем не только кованые диски в наличии, так же большое количество литых дисков в наличии, диски комплектом (4 штуки) с возможностью заказать болты и датчики давления.

Почему выбирают наш магазин дисков?
* 🖥 3D-визуализация — посмотрите, как будут выглядеть стильные литые диски на вашем авто.
* 🚚 Доставка по всей России, включая Москву, СПб, Новосибирск, Екатеринбург, Казань, Самара, Уфа, Пермь и т.д. 
* 💳 Гибкие способы оплаты: наличные, карта, Сплит, счёт с НДС.
* 🔧 Полный сервис: подбор шин, датчиков давления, консультации по параметрам литых дисков.
* 🆓 Бесплатная примерка — удобно и безопасно.
* 💼 Опыт с 2015 года — эксперты по литым и кованым дискам для кроссоверов, внедорожников и городских авто.
* 📦 Огромный выбор — от бюджетных литых дисков до эксклюзивных кованых моделей, включая литые и кованые диски на зиму.
* ⭐️ Отзывы на кованые диски подтверждают — нам доверяют тысячи клиентов.
Обратите внимание: указана цена за один диск, но продажа осуществляется только комплектом из 4 штук!

✔️ кованые диски R16 / R17 / R18 / R19 / R20 / R21 / R22 / R23 / R24
✔️ варианты под PCD 4x100, 5x108, 5×112, 5×100, 5×114.3, 4×108, 5×120, 6×139.7 и другие
✔️ модели с вылетом (offset) 35, 40, 45 и другие
✔️ подбор по марке и кузову авто — поможем выбрать литые диски под параметры автомобиля

📞 Звоните или пишите прямо сейчас, чтобы:
* заказать кованые диски,
* узнать цены и наличие,
* получить советы по выбору литых и кованых дисков,
* или просто купить диски недорого в вашем городе.'''

    return desc


def format_tire_desc_by_city_msk_piter_new(card: dict, city: str, season: str):
    """returns a formatted string with tire description for the
        offline showrooms.

    :param card: a tire card.
    :param city: a string with name of xml file.
    :param season: a tire seasonality.
    :return: a string.
    """
    city_text = ''
    if city == 'avito_msk_new.xml':
        city_text = "🛞Предоставляем услуги <strong>ШИНОМОНТАЖА,</strong> правку дисков, ремонт шин (все виды ремонта), сезонное хранение шин и дисков\n"
    
    desc = f'''Купить Нoвые Зимние шины {card["Title"]}

Пиши "Хочу шины. Укажи мapку, год aвто." и получи пoдбopку шин бесплатно!

<strong>▪️Цена указан за один шину</strong>

🔥Новые шины отличного качества!
-Усиленный борт
-Хороший баланс
-Низкий уровень шума

<strong>Если вы нашли дешевле!?
Присылайте ссылку менеджеру в чат, согласуем индивидуальное предложение!</strong>

Доставка:
▪️самовывоз;
▪️по России тк Деловые Линии, ПЭК, Энергия, КИТ.

📍 На связи каждый день с 09.00 до 20:00 по МСК времени.
{city_text}
Варианты оплаты:
▪️ на карту Сбербанк, ВТБ, Тинькофф, Альфа банк;
▪️ на расчётный счет, работаем с Юр.лицами и НДС;
▪️ наложенный платёж, Яндекс-kassa.

Пишите, звоните в любое время суток. Точную стоимость комплекта уточняйте у менеджеров.'''

    return desc


def format_alloy_rim_desc_tumen(title: str, pcd=''):
    """returns a formatted string with the alloy rim description for
        tumen showrooms.

    :param title: a string with the rim title from database.
    :param pcd: a string with rim pcd.
    :return: a string.
    """
    pcd_text = ''
    if pcd != '':
        pcd_text = PCD_DICT.get(pcd, '')



    desc = f'''{title}.

Купить литые диски в Default – самый большой ассортимент дисков на любую машину!
✅ ПРОФЕССИОНАЛЬНО ПОДБЕРЕМ литые диски и шины на ваше авто. Опыт в подборе более 10 лет, решаем самые сложные задачи.
✅ РАБОТАЕМ НАПРЯМУЮ С ЗАВОДАМИ, без посредников, лучшее соотношение цены и качества, не экономим на металле и покраске. Заводская гарантия, при вас проверим и покрутим на станке диски перед установкой.
✅ Есть РАССРОЧКА
✅ Примерим диски на машину в магазине или сделаем онлайн 3D-визуализацию.



Почему выбирают Default?
С 2015 года Default – эксперты в подборе и производстве, литых и кованых дисков и шин. Мы сотрудничаем с ведущими мировыми заводами, чтобы предложить качество, стиль и доступные цены.

Наши преимущества:
✅ Индивидуальность: 3D-визуализация покажет, как стильные литые диски преобразят ваш автомобиль, делая его ярким и заметным в потоке. Цвет дисков на экране может слегка отличаться от реальности – проверяйте при естественном свете.
✅ Полный сервис: Подбор шин, датчики давления.
✅ Гибкая оплата: Рассрочка, наличные, банковской картой, кредитной картой, расчетный счет (без НДС). 💳
✅ Прозрачные условия: Возврат возможен если вы не произвели шиномонтаж и при отсутствии повреждений.
✅ Доверие клиентов: Тысячи положительных отзывов и 10 лет опыта. 🏆

Преобразите авто с Default! Ваш стиль - наша забота!
Хотите, чтобы ваш автомобиль выглядел уникально? Литые и кованые диски от Default подчеркнут ваш стиль и идеально подойдут вашей автотомобилю. Бесплатная примерка и 3D-визуализация гарантируют точную посадку и уверенность в выборе.

{pcd_text}

Eщe бoльше литых и кованых диcкoв доcтупно нa нашeм сайте Default.ru. Наши специалисты с удовольствием проконсультируют вас и помогут с выбором!
'''

    return desc



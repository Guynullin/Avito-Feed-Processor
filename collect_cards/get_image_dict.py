import requests
import logging
import time
import re

from typing import Dict, List, Optional
from bs4 import BeautifulSoup

def get_image_dict(sitemap_url: str, slugs_list: Optional[List[str]] = None) -> Dict[str, List[str]]:
    """Fetches a sitemap XML and extracts a dictionary mapping product slugs to their image URLs.
    
    :param sitemap_url (str): The URL of the sitemap to parse.
    :param slugs_list (Optional[List[str]]): A list of product slugs to filter the results. 
        If None, all slugs are processed.

    :return Dict[str, List[str]]: A dictionary where keys are product slugs and values are lists of image URLs.
        Returns an empty dictionary if an error occurs or no data is found.
    """
    MAX_RETRIES = 7
    TIMEOUT = 120
    DELAY_BETWEEN_RETRIES = 3
    slug_dict: Dict[str, List[str]] = {}

    with requests.Session() as session:
        for attempt in range(1, MAX_RETRIES + 1):
            logging.debug(f"<get_image_dict> Attempt {attempt} for {sitemap_url}")
            
            try:
                response = session.get(sitemap_url, timeout=TIMEOUT)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"<get_image_dict> Attempt {attempt}: Failed to fetch {sitemap_url} - {e}")
                time.sleep(DELAY_BETWEEN_RETRIES)
                continue  

            try:
                soup = BeautifulSoup(response.content, 'lxml-xml')
            except Exception as e:
                logging.warning(f"<get_image_dict> Failed to parse XML from {sitemap_url} - {e}")
                continue

            url_tags = soup.find_all('url')
            if not url_tags:
                logging.warning(f"<get_image_dict> No <url> tags found in sitemap {sitemap_url}")
                continue

            for url_tag in url_tags:
                loc_tag = url_tag.find('loc')
                if not loc_tag or not loc_tag.text:
                    continue

                loc_text = loc_tag.text.strip()
                slug = loc_text.rstrip('/').split('/')[-1]  

                if slugs_list is not None and slug not in slugs_list:
                    continue

                image_tags = url_tag.find_all('image:loc')
                if not image_tags:
                    continue

                image_urls = [img_tag.text.strip() for img_tag in image_tags if img_tag.text]

                if image_urls:
                    slug_dict[slug] = image_urls

            break  

    if slug_dict:
        logging.info(f'<get_image_dict> Retrieved {len(slug_dict)} slugs from {sitemap_url}')
    else:
        logging.error(f'<get_image_dict> No image URLs found for {sitemap_url}')

    return slug_dict


def get_image_dict_wm(url: str) -> Dict[str, str]:
    """
    Fetches a product sitemap XML and extracts a dictionary mapping product IDs to their image URLs.

    :param url (str): The URL of the product sitemap to parse.

    :return Dict[str, str]: A dictionary where keys are product IDs and values are concatenated image URLs separated by '|'.
        Returns an empty dictionary if an error occurs or no data is found.
    """
    BASE_URL = 'https://default.ru'
    MAX_RETRIES = 7
    TIMEOUT = 30  # seconds
    DELAY_BETWEEN_RETRIES = 3  # seconds
    image_dict: Dict[str, str] = {}
    id_pattern = re.compile(r'^\d+$')  

    with requests.Session() as session:
        for attempt in range(1, MAX_RETRIES + 1):
            logging.debug(f"<get_image_dict_wm> Attempt {attempt} for {url}")
            try:
                response = session.get(url=url, timeout=TIMEOUT)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"<get_image_dict_wm> Attempt {attempt}: Failed to fetch {url} - {e}")
                if attempt < MAX_RETRIES:
                    time.sleep(DELAY_BETWEEN_RETRIES)
                continue

            try:
                soup = BeautifulSoup(response.content, 'lxml-xml') 
            except Exception as e:
                logging.warning(f"<get_image_dict_wm> Failed to parse XML from {url} - {e}")
                if attempt < MAX_RETRIES:
                    time.sleep(DELAY_BETWEEN_RETRIES)
                continue

            products = soup.find_all('product')
            if not products:
                logging.warning(f"<get_image_dict_wm> No <product> tags found in sitemap {url}")
                if attempt < MAX_RETRIES:
                    time.sleep(DELAY_BETWEEN_RETRIES)
                continue

            for product in products:
                id_tag = product.find('id')
                if not id_tag or not id_tag.text:
                    logging.debug(f"<get_image_dict_wm> Missing <id> tag in product.")
                    continue

                product_id = id_tag.text.strip()
                if not id_pattern.match(product_id):
                    logging.debug(f"<get_image_dict_wm> Invalid product ID format: {product_id}")
                    continue

                img_list: List[str] = []

                main_pic_tag = product.find('main_pic')
                if main_pic_tag and main_pic_tag.text:
                    main_pic = main_pic_tag.text.strip()
                    if not main_pic.startswith('http'):
                        main_pic = BASE_URL + main_pic
                    img_list.append(main_pic)

                additional_pics_tag = product.find('additional_pics')
                if additional_pics_tag:
                    pic_tags = additional_pics_tag.find_all('pic')
                    for pic in pic_tags:
                        if pic.text:
                            pic_url = pic.text.strip()
                            if not pic_url.startswith('http'):
                                pic_url = BASE_URL + pic_url
                            if not pic_url in img_list:
                                img_list.append(pic_url)

                if img_list:
                    image_dict[product_id] = '|'.join(img_list[:10])

            break

    if image_dict:
        logging.info(f'<get_image_dict_wm> Retrieved {len(image_dict)} products from {url}')
    else:
        logging.error(f'<get_image_dict_wm> No image URLs found for {url}')

    return image_dict
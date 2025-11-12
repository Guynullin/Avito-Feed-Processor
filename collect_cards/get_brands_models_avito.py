import logging
import requests

from bs4 import BeautifulSoup

def get_avito_tyre_brands(url: str):
    """returns a list containing tyre brands supported by avito.

    :param url: A string with url to avito brands xml.
    :return: a dict with avito tyre brands and models or zero when error occured.
    """
    
    resp = requests.get(url)

    if resp.status_code != 200:
        logging.error(f"<get_avito_tyre_brands> resp.status_code: {resp.status_code}")
    
    soup = BeautifulSoup(resp.content, 'xml')

    brands_dict = {}
    brands_list = soup.find_all('make')

    if brands_list and len(brands_list) > 0:
        for item in brands_list:
            name = item.get("name")
            brands_dict[name] = []
            models = item.find_all("model")
            if models and len(models) > 0:
                for model in models:
                    model_name = model.get('name')
                    brands_dict[name].append(model_name)

    if len(brands_dict) > 0:
        return brands_dict
    else:
        return 0








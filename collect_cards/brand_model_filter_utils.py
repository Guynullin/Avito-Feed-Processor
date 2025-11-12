import re
import logging
import requests
from typing import List, Dict, Optional, Union, Set, Tuple
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Tuple, Optional, Dict, Set
from difflib import SequenceMatcher



def load_allowed_rim_brands_and_models(session: requests.Session, headers: Dict[str, str]):
    """
    Loads allowed rim brands and models from the specified URLs.
    
    :param session: Requests session
    :param headers: Request headers
    :return: dictionary with brand and models if successful, None otherwise
    """
    rim_models_dict = {}
    
    # brands_url = "https://www.avito.ru/web/1/autoload/user-docs/category/67018/field/157600/values-xml"
    models_url = "https://www.avito.ru/web/1/catalogs/content/feed/rims_make.xml"
    
    try:
        # Load brands
        # response_brands = session.get(brands_url, headers=headers, timeout=30)
        # response_brands.raise_for_status()
        # brands_soup = BeautifulSoup(response_brands.content, 'xml')
        
        # rim_brands_set = set()
        # for value in brands_soup.find_all('RimBrand'):
        #     if value.text.strip():
        #         rim_brands_set.add(value.text.strip())
        
        # Load brands and models

        response_models = session.get(models_url, headers=headers, timeout=30)
        response_models.raise_for_status()
        models_soup = BeautifulSoup(response_models.content, 'xml')
        rim_models_dict = {}
        for make in models_soup.find_all('marka'):
            brand_name = make.get('name', '').strip()
            if brand_name:
                rim_models_dict[brand_name] = set()
                for model in make.find_all('model'):
                    model_name = model.get('name', '').strip()
                    if model_name:
                        rim_models_dict[brand_name].add(model_name)
        
        return rim_models_dict
        
    except requests.RequestException as e:
        logging.error(f"Failed to load allowed rim brands and models: {e}")
        return None
    

def find_closest_match(target: str, candidates: Set[str], threshold: float = 0.8) -> Optional[str]:
    """
    Finds the most similar string among candidates.
    
    :param target: Target string to search for
    :param candidates: Set of candidate strings
    :param threshold: Similarity threshold (0-1)
    :return: Most similar candidate or None if no match meets the threshold
    """
    if not target or not candidates:
        return None
    
    normalized_target = normalize_string(target)
    
    best_match = None
    best_score = 0.0
    
    for candidate in candidates:
        normalized_candidate = normalize_string(candidate)
        
        score = SequenceMatcher(None, normalized_target, normalized_candidate).ratio()
        
        if score > best_score and score >= threshold:
            best_score = score
            best_match = candidate
    
    return best_match if best_match else None

def normalize_string(s: str) -> str:
    """
    Normalizes a string for comparison: converts to lowercase,
    removes special characters and extra spaces.
    
    :param s: Input string
    :return: Normalized string
    """
    if not s:
        return ""
    
    normalized = s.lower()
    normalized = re.sub(r'[^\w\s]', '', normalized)
    normalized = re.sub(r'\s+', ' ', normalized)
    
    return normalized.strip()

def match_rim_brand_and_model(
    valid_brands_models: Dict[str, Set[str]],
    input_brand: Optional[str],
    input_model: Optional[str],
    brand_threshold: float = 0.7,
    model_threshold: float = 0.8
) -> Tuple[Optional[str], Optional[str]]:
    """
    Matches input brand and model with valid values from the dictionary.
    
    :param valid_brands_models: Dictionary of valid brands and their models
    :param input_brand: Input brand to match
    :param input_model: Input model to match
    :param brand_threshold: Similarity threshold for brand matching
    :param model_threshold: Similarity threshold for model matching
    :return: Tuple of (matched_brand, matched_model) or (None, None) if no match
    """
    if not valid_brands_models or not input_brand:
        return 'Default', None
    
    valid_brands = set(valid_brands_models.keys())
    pattern = r'\s*в\s+стиле\s*'
    clear_brand = re.sub(pattern, ' ', input_brand, flags=re.IGNORECASE).strip()
    matched_brand = find_closest_match(clear_brand, valid_brands, brand_threshold)
    
    if not matched_brand:
        return 'Default', None
    
    if not input_model:
        return matched_brand, None
    
    valid_models = valid_brands_models[matched_brand]
    matched_model = find_closest_match(input_model, valid_models, model_threshold)
    
    return matched_brand, matched_model


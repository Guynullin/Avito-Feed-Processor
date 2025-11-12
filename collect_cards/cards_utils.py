import logging

from urllib.parse import urljoin, urlparse
from typing import Optional


def construct_full_url(root_url: str, path: str) -> Optional[str]:
    """
    Constructs a full URL by properly joining the root URL and the image path.

    :param root_url: The root URL, e.g., "https://example.com" or "https://example.com/".
    :param path: The image path, e.g., "/path_to_image.jpg" or "path_to_image.jpg".
    :return: A properly formatted URL or None if the path is invalid.
    """
    if not root_url or not path:
        logging.warning("<construct_full_url> Empty root_url or path.")
        return None

    if path.lower().startswith(('http://', 'https://')):
        return path if urlparse(path).netloc else None
    try:
        return urljoin(root_url, path)
    except Exception as e:
        logging.error(f"<construct_full_url> Error constructing URL from root '{root_url}' and path '{path}': {e}")
        return None
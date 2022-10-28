from json import JSONDecodeError
from typing import Any, Dict, List, Tuple

import requests


def get_request(url: str, *args, **kwargs) -> Dict[str, Any]:
    """
    Takes in the url and additional args/kwargs. Performs a
    get request and returns the results as a dictionary.

    Args:
        url (str): _description_

    Raises:
        SystemExit: returns the request exception
        SystemExit: returns the json decode exception

    Returns:
        Dict[str, Any]: response as a dictionary
    """
    try:
        response = requests.get(url=url, headers=kwargs)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    try:
        response_dict = response.json()
    except JSONDecodeError as e:
        raise SystemExit(e)
    return response_dict


def item_generator(json_input: Dict[str, Any], lookup_key: str) -> Any:
    """Recursively iterates through a dictionary looking
    for a given key. When found, returns the key value

    Args:
        json_input (Dict[str, Any]): the dictionary input
        lookup_key (str): the key to look for

    Yields:
        Any: the value for the given key
    """
    if isinstance(json_input, dict):
        for key, value in json_input.items():
            if key == lookup_key:
                yield value
            else:
                yield from item_generator(value, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

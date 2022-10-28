from typing import Any, Dict

from config import Config
from utils.utility import get_request, item_generator


def get_lat_long(city: str) -> Dict[str, Any]:
    """
    1. Creates the GET URL
    2. Performs the GET request
    3. Recursively walks the response dictionary looking for
    the given key
    4. The desired value to the given city

    Args:
        city (str): city to get the
        latitude/longitude

    Returns:
        Dict[str, Any]: The given city and it's latitude/longitude
    """

    response = get_request(
        url=Config.GOOGLE_MAPS_BASE_URL
        + f"?address={city}&key={Config.GOOGLE_MAPS_API_KEY}"
    )
    location = next(item_generator(response, "location"))
    return location

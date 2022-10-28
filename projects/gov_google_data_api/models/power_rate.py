from typing import Any, Dict

from config import Config
from utils.utility import get_request


def get_power_rate(location: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes a GET request in order to extract power rates and metadata for the given
    latitude and longitude

    Args:
        location (Dict[str, Any]): Dictionary containing Latitude/Longitude

    Raises:
        SystemExit: Exits the interpretter and raises the given error

    Returns:
        dict: response in dictionary format
    """
    parameters = f"?api_key={Config.GOV_API_KEY}&region=tract&id=101&lat={location['lat']}&lon={location['lng']}"
    url = Config.GOV_BASE_API + parameters
    response_dict = get_request(url)

    return response_dict

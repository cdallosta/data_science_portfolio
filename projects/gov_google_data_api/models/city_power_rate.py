from flask import Blueprint

from .google_maps import get_lat_long
from .power_rate import get_power_rate

city_power_rate_api = Blueprint("city_power_rate_api", __name__)


@city_power_rate_api.route("/city_power_rate/<city>", methods=["GET"])
def get_city_power_rate(city: str):
    """
    Takes in a city and calls the get_lat_long to return the latitude
    and longitude of the city. Passes data to get_power_rate callable.
    Returns the metadata for a given cities power and power rate

    Args:
        city (str): the given city

    Returns:
        json: returns a jsonified dictionary
    """
    city_location = get_lat_long(city)
    power_rate_meta_list = get_power_rate(city_location)
    return power_rate_meta_list

from flask import Blueprint, jsonify
from models.city_power_rate import get_city_power_rate

city_power_rate_api = Blueprint("city_power_rate_api", __name__)


@city_power_rate_api.route("/city_power_rate/<city>", methods=["GET"])
def get(city: str):
    """
    API Endpoint that takes in a city and calls the get_city_power_rate
    callable.

    Args:
        city (str): the given city

    Returns:
        json: returns a jsonified dictionary
    """

    response = get_city_power_rate(city)
    return jsonify(response, 200)

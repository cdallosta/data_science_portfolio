from typing import Any, Dict, List, Tuple

from flask import Blueprint, jsonify
from models.power_rate import get_power_rate

power_rate_api = Blueprint("power_rate_api", __name__)


@power_rate_api.route("/power_rate/<location>", methods=["GET"])
def get(location: Dict[str, Any]):
    """
    API Endpoint that takes in a dictionary containg the latitude
    and longitude for a city. Calls the get_power_rate callable

    Args:
        location (Dict[str, Any]): the latitude and longitude of
        a city

    Returns:
        json: returns a jsonified dictionary
    """
    response = get_power_rate(location)
    return jsonify(response, 200)

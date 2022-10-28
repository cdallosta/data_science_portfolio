from typing import Any, Dict, List, Tuple

from flask import Blueprint, abort, jsonify, make_response
from models.google_maps import get_lat_long

google_maps_api = Blueprint("google_maps_api", __name__)


@google_maps_api.route("/api")
@google_maps_api.route("/google_maps/<city>", methods=["GET"])
def get(city: str):
    """
    API Endpoint that takes in a city and calls the get_lat_long
    callable to return the latitude and longitude of a given
    city

    Args:
        city (str): the given city

    Returns:
        json: returns a jsonified dictionary
    """
    response = get_lat_long(city)
    response = make_response(jsonify(response), 200)
    return response

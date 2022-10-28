from typing import Any, Dict, List, Tuple

from flask import Blueprint, jsonify
from flask_restful import Resource
from models.city_power_rate import get_city_power_rate
from models.google_maps import get_lat_long

city_power_rate_api = Blueprint("city_power_rate_api", __name__)


@city_power_rate_api.route("/city_power_rate/<city>", methods=["GET"])
def get(city: str) -> json:

    response = get_city_power_rate(city)
    return jsonify(response, 200)

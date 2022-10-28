import logging

from flask import Flask

from config import Config
from routes.city_power_rate import city_power_rate_api
from routes.google_maps import google_maps_api


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    app.register_blueprint(google_maps_api, url_prefix="/api")
    app.register_blueprint(city_power_rate_api, url_prefix="/api")
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=False)

from os import getenv

from dotenv import find_dotenv, load_dotenv


class Config:
    load_dotenv(find_dotenv())
    GOV_API_KEY = getenv("GOV_API_KEY")
    GOOGLE_MAPS_API_KEY = getenv("GOOGLE_MAPS_API_KEY")
    GOOGLE_MAPS_BASE_URL = getenv("GOOGLE_MAPS_BASE_URL")
    GOV_BASE_API = getenv("GOV_BASE_API")

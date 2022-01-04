from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    VENDOR_URL = environ.get("VENDOR_URL")
    LOCALE = environ.get("LOCALE")
    X_RAPID_API_HOST = environ.get("X_RAPID_API_HOST")
    X_RAPID_API_KEY = environ.get("X_RAPID_API_KEY")

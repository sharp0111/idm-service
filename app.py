"""APP"""
from flask import Flask, request

from config.config import Config
from api.route import VendorService

app = Flask(__name__)

vendorService = VendorService(
    Config.VENDOR_URL, Config.LOCALE, Config.X_RAPID_API_HOST, Config.X_RAPID_API_KEY)


@app.route("/")
def hello_world():
    """Hello World"""
    return "<p>Hello, World!</p>"


@app.route("/search", methods=["GET"])
def search():
    """Search"""
    return vendorService.search(request.args)


@app.route("/auto-complete", methods=["GET"])
def auto_complete():
    """Auto-Complete"""
    return vendorService.auto_complete(request.args)


@app.route("/songs/details", methods=["GET"])
def get_song_details():
    """GET song details"""
    return vendorService.get_song_details(request.args)

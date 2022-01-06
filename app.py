"""APP"""
from flask import Flask, request

from config.config import Config
from api.route import VendorService

app = Flask(__name__)

vendorService = VendorService(
    Config.VENDOR_URL, Config.LOCALE, Config.X_RAPID_API_HOST, Config.X_RAPID_API_KEY)


@app.route("/search", methods=["GET"])
def search():
    """Search"""
    return vendorService.search(request.args)


@app.route("/auto-complete", methods=["GET"])
def auto_complete():
    """Auto-Complete"""
    return vendorService.auto_complete(request.args)


@app.route("/songs/details", methods=["GET"])
def fetch_song_details():
    """GET song details"""
    return vendorService.fetch_song_details(request.args)


@app.route("/songs/recommendations", methods=["GET"])
def fetch_song_recommendations():
    """GET song recommendations"""
    return vendorService.fetch_song_recommendations(request.args)

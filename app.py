"""APP"""
from flask import Flask, request

from config.config import Config
from api.route import VendorService

app = Flask(__name__)

vendorService = VendorService(
    Config.VENDOR_URL, Config.LOCALE, Config.X_RAPID_API_HOST, Config.X_RAPID_API_KEY)


@app.route("/search", methods=["GET"])
def search():
    """Search for songs, artists that match input term"""
    return vendorService.search(request.args)


@app.route("/auto-complete", methods=["GET"])
def auto_complete():
    """Get suggestions by word or phrase"""
    return vendorService.auto_complete(request.args)


@app.route("/songs/details", methods=["GET"])
def fetch_song_details():
    """Get details information of specific song"""
    return vendorService.fetch_song_details(request.args)


@app.route("/songs/recommendations", methods=["GET"])
def fetch_song_recommendations():
    """List related ones to a specific song"""
    return vendorService.fetch_song_recommendations(request.args)


@app.route("/songs/artist-top-tracks", methods=["GET"])
def fetch_song_artist_top_tracks():
    """List top tracks of specific artist"""
    return vendorService.fetch_song_artist_top_tracks(request.args)


@app.route("/songs/count", methods=["GET"])
def fetch_song_count():
    """Get total times the specific song is detected by using …/songs/detect endpoint"""
    return vendorService.fetch_song_count(request.args)


@app.route("/charts/list", methods=["GET"])
def fetch_chart_list():
    """List all available charts by cities, countries, and genres"""
    return vendorService.fetch_chart_list()

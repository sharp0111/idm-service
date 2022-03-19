"""APP"""
from flask import Flask, request

from config import Config
from api import ApiService

__locale = Config.LOCALE
__timezone = Config.TIMEZONE

apiService = ApiService(
    Config.VENDOR_URL, Config.X_RAPID_API_HOST, Config.X_RAPID_API_KEY)

app = Flask(__name__)


@app.route("/songs/artist-top-tracks", methods=["GET"])
def fetch_song_artist_top_tracks():
    """List top tracks of specific artist"""
    return apiService.fetch_song_artist_top_tracks(request.args, __locale)


@app.route("/songs/recommendations", methods=["GET"])
def fetch_song_recommendations():
    """List related ones to a specific song"""
    return apiService.fetch_song_recommendations(request.args, __locale)


@app.route("/songs/idm", methods=["POST"])
def idm():
    """Detect songs from raw sound data.
    The raw sound data must be 44100Hz, 1 channel (Mono), signed 16 bit PCM
    """
    return apiService.idm(request, __timezone, __locale)


@app.route("/songs/details", methods=["GET"])
def fetch_song_details():
    """Get details information of specific song"""
    return apiService.fetch_song_details(request.args, __locale)


@app.route("/songs/count", methods=["GET"])
def fetch_song_count():
    """Get total times the specific song is detected by using …/songs/idm endpoint"""
    return apiService.fetch_song_count(request.args)


@app.route("/charts/list", methods=["GET"])
def fetch_chart_list():
    """List all available charts by cities, countries, and genres"""
    return apiService.fetch_chart_list()


@app.route("/charts/track", methods=["GET"])
def fetch_chart_track():
    """Get all popular songs in specific chart"""
    return apiService.fetch_chart_track(request.args, __locale)


@app.route("/search", methods=["GET"])
def search():
    """Search for songs, artists that match input term"""
    return apiService.search(request.args, __locale)


@app.route("/auto-complete", methods=["GET"])
def auto_complete():
    """Get suggestions by word or phrase"""
    return apiService.auto_complete(request.args, __locale)

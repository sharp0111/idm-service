"""Main Route File"""
import requests


class VendorService:
    """ VendorService """

    def __init__(self, vendor_url: str, locale: str, vendor_api_host: str, vendor_api_key: str):
        self.vendor_url = vendor_url
        self.locale = locale
        self.x_rapid_api_host = vendor_api_host
        self.x_rapid_api_key = vendor_api_key

    def search(self, req):
        """Search for songs, artists that match input term"""
        term_param = req.get("term")
        params = {"term": term_param, "locale": self.locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/search",
                           headers=headers, params=params)
        return res.json()

    def auto_complete(self, req):
        """Get suggestions by word or phrase"""
        term_param = req.get("term")
        params = {"term": term_param, "locale": self.locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/auto-complete",
                           headers=headers, params=params)
        return res.json()

    def fetch_song_details(self, req):
        """Get details information of specific song"""
        key_param = req.get("key")
        params = {"key": key_param, "locale": self.locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/songs/get-details",
                           headers=headers, params=params)
        return res.json()

    def fetch_song_recommendations(self, req):
        """List related ones to a specific song"""
        key_param = req.get("key")
        params = {"key": key_param, "locale": self.locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/songs/list-recommendations",
                           headers=headers, params=params)
        return res.json()

    def fetch_song_artist_top_tracks(self, req):
        """List top tracks of specific artist"""
        id_param = req.get("id")
        params = {"id": id_param, "locale": self.locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/songs/list-artist-top-tracks",
                           headers=headers, params=params)
        return res.json()

    def fetch_song_count(self, req):
        """Get total times the specific song is detected by using …/songs/detect endpoint"""
        key_param = req.get("key")
        params = {"key": key_param}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/songs/get-count",
                           headers=headers, params=params)
        return res.json()

    def fetch_chart_list(self):
        """List all available charts by cities, countries, and genres"""
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/charts/list",
                           headers=headers)
        return res.json()

    def __get_headers(self):
        """Header Parameters"""
        return {"X-RapidAPI-Host": self.x_rapid_api_host,
                "X-RapidAPI-Key": self.x_rapid_api_key}

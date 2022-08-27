"""ApiService"""
import requests


class ApiService:
    """ ApiService """

    def __init__(self, vendor_url: str, vendor_api_host: str, vendor_api_key: str):
        self.vendor_url = vendor_url
        self.x_rapid_api_host = vendor_api_host
        self.x_rapid_api_key = vendor_api_key

    def __get_headers(self):
        """Header Parameters"""
        return {"X-RapidAPI-Host": self.x_rapid_api_host,
                "X-RapidAPI-Key": self.x_rapid_api_key}

    def fetch_song_artist_top_tracks(self, req, locale):
        """List top tracks of specific artist"""
        # The id field inside artists json object returned from …/songs/detect or …/search endpoint
        id_param = req.get("id")
        params = {"id": id_param, "locale": locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/songs/list-artist-top-tracks",
                           headers=headers, params=params)
        return res.json()

    def fetch_song_recommendations(self, req, locale):
        """List related ones to a specific song"""
        # The key field returned from …/songs/detect or …/search endpoint
        key_param = req.get("key")
        params = {"key": key_param, "locale": locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/songs/list-recommendations",
                           headers=headers, params=params)
        return res.json()

    def detect(self, req, timezone, locale):
        """Detect songs from raw sound data.
        The raw sound data must be 44100Hz, 1 channel (Mono), signed 16 bit PCM
        """
        print("Hitting POST")
        payload = req.data
        print(payload)
        headers = self.__get_headers()
        params = {"timezone": timezone, "locale": locale}
        res = requests.post(self.vendor_url + "/songs/v2/detect",
                            data=payload, headers=headers, params=params)
        return res.json()

    def fetch_song_details(self, req, locale):
        """Get details information of specific song"""
        # The key field returned from …/songs/detect or …/search endpoint
        key_param = req.get("key")
        params = {"key": key_param, "locale": locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/songs/get-details",
                           headers=headers, params=params)
        return res.json()

    def fetch_song_count(self, req):
        """Get total times the specific song is detected by using …/songs/detect endpoint"""
        # The key field returned from …/songs/detect or …/search endpoint
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

    def fetch_chart_track(self, req, locale):
        """Get all popular songs in specific chart"""
        # The value of listId field returned in …/charts/list endpoint
        list_id_param = req.get("listId")
        # Used for paging purpose, 20 items per response is maximum.
        page_size_param = req.get("pageSize")
        # Used for paging purpose.
        start_from_param = req.get("startFrom")
        optional_params = {"locale": locale, "listId": list_id_param,
                           "pageSize": page_size_param, "startFrom": start_from_param}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/charts/track",
                           headers=headers, params=optional_params)
        return res.json()

    def search(self, req, locale):
        """Search for songs, artists that match input term"""
        term_param = req.get("term")
        offset_param = req.get("offset")
        limit_param = req.get("limit")
        params = {"term": term_param, "locale": locale,
                  "offset": offset_param, "limit": limit_param}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/search",
                           headers=headers, params=params)
        return res.json()

    def auto_complete(self, req, locale):
        """Get suggestions by word or phrase"""
        term_param = req.get("term")
        params = {"term": term_param, "locale": locale}
        headers = self.__get_headers()
        res = requests.get(self.vendor_url + "/auto-complete",
                           headers=headers, params=params)
        return res.json()

"""Main Route File"""
import requests


class VendorService:
    """ VendorService """

    def __init__(self, vendor_url, locale, vendor_api_host, vendor_api_key):
        self.vendor_url = vendor_url
        self.locale = locale
        self.x_rapid_api_host = vendor_api_host
        self.x_rapid_api_key = vendor_api_key

    def search(self, term):
        """Search"""
        params = {"term": term, "locale": self.locale}
        headers = {"X-RapidAPI-Host": self.x_rapid_api_host,
                   "X-RapidAPI-Key": self.x_rapid_api_key}
        res = requests.get(self.vendor_url + "/search",
                           headers=headers, params=params)
        return res.json()

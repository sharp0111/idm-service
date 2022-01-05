"""Main Route File"""
import requests


class VendorService:
    """ VendorService """

    def __init__(self, vendor_url: str, locale: str, vendor_api_host: str, vendor_api_key: str):
        self.vendor_url = vendor_url
        self.locale = locale
        self.x_rapid_api_host = vendor_api_host
        self.x_rapid_api_key = vendor_api_key

    def search(self, term: str):
        """Search"""
        params = self.get_params(term)
        headers = self.get_headers()
        res = requests.get(self.vendor_url + "/search",
                           headers=headers, params=params)
        print(res)
        return res.json()

    def auto_complete(self, term: str):
        """Auto-Complete"""
        params = self.get_params(term)
        headers = self.get_headers()
        res = requests.get(self.vendor_url + "/auto-complete",
                           headers=headers, params=params)
        print(res)
        return res.json()

    def get_params(self, term: str):
        """Get Params"""
        return {"term": term, "locale": self.locale}

    def get_headers(self):
        """Get Headers"""
        return {"X-RapidAPI-Host": self.x_rapid_api_host,
                "X-RapidAPI-Key": self.x_rapid_api_key}

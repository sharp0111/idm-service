import requests


class VendorService:

    def __init__(self, vendorUrl, locale, vendorApiHost, vendorApiKey):
        self._vendorUrl = vendorUrl
        self._locale = locale
        self._XRapidAPIHost = vendorApiHost
        self._XRapidAPIKey = vendorApiKey

    def search(self, term):
        params = {"term": term, "locale": self._locale}
        headers = {"X-RapidAPI-Host": self._XRapidAPIHost,
                   "X-RapidAPI-Key": self._XRapidAPIKey}
        r = requests.get(self._vendorUrl + "/search",
                         headers=headers, params=params)
        return r.json()

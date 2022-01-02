import requests


class VendorService:

    _vendorUrl = "https://shazam.p.rapidapi.com"
    _locale = "en-US"
    _XRapidAPIHost = "shazam.p.rapidapi.com"
    _XRapidAPIKey = "d63ad138d7mshcce2e1a50baf88ep182504jsne40f42ff497a"

    def search(self, term):
        params = {"term": term, "locale": self._locale}
        headers = {"X-RapidAPI-Host": self._XRapidAPIHost,
                   "X-RapidAPI-Key": self._XRapidAPIKey}
        r = requests.get(self._vendorUrl + "/search",
                         headers=headers, params=params)
        return r.json()

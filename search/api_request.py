import requests
from search.google.google_exceptions import GoogleException


class ApiRequest:
    def __init__(self, url, params, query_param_name):
        self.url = url
        self.params = params
        self.query_param_name = query_param_name

    def request(self, query):
        self.params[self.query_param_name] = query
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            return response.content
        else:
            raise GoogleException('API returned error code ', response.status_code)

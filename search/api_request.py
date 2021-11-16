import requests
from search.exceptions import ApiException


class ApiRequest:
    """
    A class that represents a GET request to some search api
    :attribute url: The URL of the API
    :attribute params: The parameters of a GET-request
    :attribute query_param_name: The name of the parameter,
    which value will contain the search query
    :method request: Performs the request to the API
    """
    def __init__(self, url: str, params: dict, query_param_name: str):
        self.url = url
        self.params = params
        self.query_param_name = query_param_name

    def request(self, query: str):
        """
        Performs a GET request to the URL, with the specified params,
        one of which is query
        :param query: Search query to pass to the API
        """
        self.params[self.query_param_name] = query
        response = requests.get(self.url, params=self.params)
        if response.status_code == 200:
            return response.content
        else:
            raise ApiException('API returned error code ' + response.status_code)

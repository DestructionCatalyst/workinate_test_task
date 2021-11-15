import search.serpapi_yandex.confidential as confidential
from search.api_request import ApiRequest


yandex_serpapi_request = ApiRequest(url='https://serpapi.com/search.json',
                                params={'engine': 'yandex',
                                        'api_key': confidential.apikey},
                                query_param_name='text')
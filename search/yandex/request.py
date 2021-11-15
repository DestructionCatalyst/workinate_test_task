import search.yandex.confidential as confidential
from search.api_request import ApiRequest


yandex_api_request = ApiRequest(url='https://yandex.com/search/xml',
                                params={'l10n': 'en',
                                        'user': confidential.user,
                                        'key': confidential.apikey},
                                query_param_name='query')
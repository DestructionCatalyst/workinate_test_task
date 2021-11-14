import os
from django.conf import settings
import search.yandex.confidential as confidential
from search.api_request import ApiRequest


def yandex_search_api_request(query: str):
    file_path = os.path.join(settings.BASE_DIR, 'search', 'yandex', 'test_response.xml')
    with open(file_path) as xml_file:
        xml_string = xml_file.read()

    return xml_string

yandex_api_request = ApiRequest(url='https://yandex.com/search/xml',
                                params={'l10n': 'en',
                                        'user': confidential.user,
                                        'key': confidential.apikey},
                                query_param_name='query')
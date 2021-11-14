import search.google.confidential as confidential
from search.api_request import ApiRequest


google_api_request = ApiRequest(url='https://www.googleapis.com/customsearch/v1',
                                params={'key': confidential.apikey,
                                         'cx': confidential.cx},
                                query_param_name='q')
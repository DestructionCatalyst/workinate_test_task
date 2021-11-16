from search.base_response_formatter import BaseResponseFormatter
from search.exceptions import ApiException
import json


class SerpapiResponseFormatter(BaseResponseFormatter):
    def parse_input(self):
        try:
            json_dict = json.loads(self.input_data)
        except json.JSONDecodeError:
            raise ApiException('Invalid response from API')
        if json_dict.get('error') is not None:
            # There is no error codes in SerpApi responces,
            # so I just had to check for string value
            if json_dict['error'] == \
                'Yandex hasn\'t returned any results for this query.':
                    return []
            raise ApiException(json_dict['error'])
        raw_items = json_dict.get('organic_results')
        if raw_items is None:
            raise ApiException('Invalid response from API')
        items = list(map(lambda item: item.get('link'), raw_items[:10]))
        return items

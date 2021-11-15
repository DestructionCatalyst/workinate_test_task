from search.base_response_formatter import BaseResponseFormatter
from search.serpapi_yandex.exceptions import SerpapiException
import json


class SerpapiResponseFormatter(BaseResponseFormatter):
    def parse_input(self):
        try:
            json_dict = json.loads(self.input_data)
        except json.JSONDecodeError:
            raise SerpapiException('Invalid response')
        if json_dict.get('error') is not None:
            if json_dict['error'] == \
                'Yandex hasn\'t returned any results for this query.':
                    return []
            raise SerpapiException(json_dict['error'])
        raw_items = json_dict.get('organic_results')
        if raw_items is None:
            raise SerpapiException('Invalid response')
        items = list(map(lambda item: item.get('link'), raw_items[:10]))
        return items

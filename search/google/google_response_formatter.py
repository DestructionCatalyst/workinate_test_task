from search.base_response_formatter import BaseResponseFormatter
from search.google.google_exceptions import GoogleException
import json


class GoogleResponseFormatter(BaseResponseFormatter):
    def parse_input(self):
        try:
            json_dict = json.loads(self.input_data)
        except json.JSONDecodeError:
            raise GoogleException('Invalid response', '502')
        raw_items = json_dict.get('items')
        if raw_items is None:
            raise GoogleException('Invalid response', '502')
        items = list(map(lambda item: item.get('link'), raw_items))
        return items

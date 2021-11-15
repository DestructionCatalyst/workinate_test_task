from search.base_response_formatter import BaseResponseFormatter
from search.google.exceptions import GoogleException
import json


class GoogleResponseFormatter(BaseResponseFormatter):
    def parse_input(self):
        try:
            json_dict = json.loads(self.input_data)
        except json.JSONDecodeError:
            raise GoogleException('Invalid response', '500')
        raw_items = json_dict.get('items')
        if raw_items is None:
            return []
        items = list(map(lambda item: item.get('link'), raw_items))
        return items

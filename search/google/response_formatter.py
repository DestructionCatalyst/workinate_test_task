from search.base_response_formatter import BaseResponseFormatter
from search.exceptions import ApiException
import json


class GoogleResponseFormatter(BaseResponseFormatter):
    def parse_input(self):
        try:
            json_dict = json.loads(self.input_data)
        except json.JSONDecodeError:
            raise ApiException('Invalid response from API')
        raw_items = json_dict.get('items')
        if raw_items is None:
            return []
        items = list(map(lambda item: item.get('link'), raw_items))
        return items

from search.base_response_formatter import BaseResponseFormatter
import json


class GoogleResponseFormatter(BaseResponseFormatter):
    def parse_input(self):
        json_dict = json.loads(self.input_data)
        raw_items = json_dict.get('items')
        items = list(map(lambda item: item.get('link'), raw_items))
        return items

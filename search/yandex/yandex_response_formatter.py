import xml.etree.ElementTree as ET
from search.yandex.yandex_exceptions import YandexException
from search.base_response_formatter import BaseResponseFormatter


def parse_group(group: ET.Element):
    doc = group.find('doc')
    url = doc.find('url')
    return url.text.strip()


class YandexResponceFormatter(BaseResponseFormatter):
    def parse_input(self):
        tree = ET.fromstring(self.input_data)
        responce = tree.find('response')
        error = responce.find('error')
        if error is not None:
            raise YandexException(
                error.text.strip(),
                error.get('code'))
        results = responce.find('results')
        grouping = results.find('grouping')
        groups = grouping.findall('group')
        return map(parse_group, groups)

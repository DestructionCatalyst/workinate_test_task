import xml.etree.ElementTree as ET
from search.yandex.exceptions import YandexException
from search.base_response_formatter import BaseResponseFormatter


def try_find_in_xml(element: ET.Element, tag: str):
    result = element.find(tag)
    if result is None:
        raise YandexException(
                'Invalid response',
                '502')
    return result


def parse_group(group: ET.Element):
    doc = try_find_in_xml(group, 'doc')
    url = try_find_in_xml(doc, 'url')
    return url.text.strip()


class YandexResponseFormatter(BaseResponseFormatter):
    def parse_input(self):
        try:
            tree = ET.fromstring(self.input_data)
        except ET.ParseError:
            raise YandexException(
                'Invalid response',
                '502')
        response = try_find_in_xml(tree, 'response')
        error = response.find('error')
        if error is not None:
            raise YandexException(
                error.text.strip(),
                error.get('code'))
        results = try_find_in_xml(response, 'results')
        grouping = try_find_in_xml(results, 'grouping')
        groups = grouping.findall('group')
        return map(parse_group, groups)

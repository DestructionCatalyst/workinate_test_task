import xml.etree.ElementTree as ET
from search.yandex.yandex_exceptions import YandexException


def parse_group(group: ET.Element):
    doc = group.find('doc')
    url = doc.find('url')
    return url.text.strip()


def parse_xml(xml):
    tree = ET.fromstring(xml)
    responce = tree.find('response')
    error = responce.find('error')
    if error is not None:
        raise YandexException(
            "Got the error message from Yandex XML",
            error.get('code'))
    results = responce.find('results')
    grouping = results.find('grouping')
    groups = grouping.findall('group')
    urls = enumerate(map(parse_group, groups), 1)
    return [{'num': num, 'url': url} for num, url in urls]


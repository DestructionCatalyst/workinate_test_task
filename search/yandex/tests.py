from search.yandex.parse_xml import parse_xml
from search.yandex.yandex_exceptions import YandexException
from django.test import TestCase
import os


class YandexTestCase(TestCase):
    def setUp(self):
        pass

    def test_xml_parsing(self):
        file_path = os.path.join('search', 'yandex', 'test_responce.xml')
        with open(file_path) as xml_file:
            xml_string = xml_file.read()
        expected = [{'num': 1, 'url': 'https://yandex.ru/'},
                    {'num': 2, 'url': 'https://yandex.ru/m/'},
                    {'num': 3, 'url': 'https://yandex.ru/news/'},
                    {'num': 4, 'url': 'https://yandex.ru/maps/'},
                    {'num': 5, 'url': 'https://yandex.com/news'},
                    {'num': 6, 'url': 'https://browser.yandex.ru/'},
                    {'num': 7, 'url': 'https://yandex.ru/all?from=tabbar'},
                    {'num': 8, 'url': 'https://yandex.ru/games/'},
                    {'num': 9, 'url': 'https://yandex.ru/video/?p=1'},
                    {'num': 10, 'url': 'https://yandex.ru/all'}]
        self.assertEqual(expected, parse_xml(xml_string))

    def test_xml_error(self):
        file_path = os.path.join('search', 'yandex', 'test_error_responce.xml')
        with open(file_path) as xml_file:
            xml_string = xml_file.read()
        with self.assertRaises(YandexException):
            parse_xml(xml_string)



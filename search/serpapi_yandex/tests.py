from search.serpapi_yandex.response_formatter import SerpapiResponseFormatter
from search.exceptions import ApiException
from unittest import TestCase
import os


class GoogleTestCase(TestCase):
    def setUp(self):
        pass

    def test_json_parsing(self):
        file_path = os.path.join('search', 'serpapi_yandex', 'test_response.json')
        with open(file_path) as json_file:
            json_string = json_file.read()
        expected = [{'num': 1, 'url': 'https://en.wikipedia.org/wiki/Coffee'},
                    {'num': 2, 'url':
                        'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%84%D0%B5'},
                    {'num': 3, 'url': 'https://Lifehacker.ru/all-about-coffee/'},
                    {'num': 4, 'url': 'https://edaplus.info/drinks/coffee.html'},
                    {'num': 5, 'url':
                        'https://www.youtube.com/watch?v=LkBOAvzWNfM'},
                    {'num': 6, 'url': 'https://WooordHunt.ru/word/coffee'},
                    {'num': 7, 'url':
                        'https://shop.tastycoffee.ru/how-to-choose-coffee'},
                    {'num': 8, 'url': 'https://t.me/s/VKCoffee'},
                    {'num': 9, 'url':
                        'https://pixabay.com/images/search/coffee/'},
                    {'num': 10, 'url': 'https://www.pexels.com/search/coffee/'}]
        self.assertEqual(expected,
            SerpapiResponseFormatter(json_string).get_formatted_response())

    def test_invalid_json(self):
        with self.assertRaisesRegex(ApiException, r'Invalid response from API'):
            SerpapiResponseFormatter('lorem ipsum').get_formatted_response()
            SerpapiResponseFormatter('{}').get_formatted_response()

    def test_empty_response(self):
         self.assertEqual([],
            SerpapiResponseFormatter(
                '{"error": "Yandex hasn\'t returned any results for this query."}'
                ).get_formatted_response())

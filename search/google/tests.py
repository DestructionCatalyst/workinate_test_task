from search.google.response_formatter import GoogleResponseFormatter
from search.exceptions import ApiException
from unittest import TestCase
import os


class GoogleTestCase(TestCase):
    def setUp(self):
        pass

    def test_json_parsing(self):
        file_path = os.path.join('search', 'google', 'test_response.json')
        with open(file_path) as json_file:
            json_string = json_file.read()
        expected = [{'num': 1, 'url': 'https://en.wikipedia.org/wiki/Lecture'},
                    {'num': 2, 'url':
                        'https://www.youtube.com/channel/UCFJyaHVyWKb2y-HkIAEPIdA'},
                    {'num': 3, 'url':
                        'https://www.cmu.edu/teaching/designteach/design/instructionalstrategies/lectures.html'},
                    {'num': 4, 'url':
                        'https://www.feynmanlectures.caltech.edu/'},
                    {'num': 5, 'url': 'https://lectures.org/'},
                    {'num': 6, 'url':
                        'https://www.brandeis.edu/mandel-center-humanities/mandel-lectures.html'},
                    {'num': 7, 'url':
                        'https://academy.allaboutbirds.org/live-events/'},
                    {'num': 8, 'url':
                        'https://www.supremecourt.gov/visiting/courtroomlectures.aspx'},
                    {'num': 9, 'url':
                        'https://www.redbullmusicacademy.com/lectures/'},
                    {'num': 10, 'url':
                        'https://www.sciarc.edu/events/lectures'}]
        self.assertEqual(expected,
            GoogleResponseFormatter(json_string).get_formatted_response())

    def test_invalid_json(self):
        with self.assertRaisesRegex(ApiException, r'Invalid response from API'):
            GoogleResponseFormatter('lorem ipsum').get_formatted_response()

    def test_empty_json(self):
        self.assertEqual([],
            GoogleResponseFormatter('{}').get_formatted_response())

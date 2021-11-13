from abc import ABC, abstractmethod

class BaseResponseFormatter(ABC):
    def __init__(self, input_data: str):
        """
        :param input_data: a string that will be processed.
        It should have some markup language format.
        """
        self.input_data = input_data

    @abstractmethod
    def parse_input(self):
        """
        Transforms self.input_data into URLs of search results.
        :returns: An iterable of URLs extracted from self.input_data
        """
        pass

    def get_formatted_response(self):
        """
        Transforms self.input_data into a list of dictionaries with keys
        'num' and 'url'. The value of 'num' is index of a search result,
        the value of 'url' is the URL of the website provided by a search engine
        :returns: The dictionary in the specified format
        """
        urls = self.parse_input()
        return [{'num': num, 'url': url} for num, url in enumerate(urls, 1)]

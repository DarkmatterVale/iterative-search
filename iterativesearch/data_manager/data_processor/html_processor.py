from .data_processor import DataProcessor
from bs4 import BeautifulSoup

class HTMLDataProcessor(DataProcessor):

    def process(self, raw_data, **kwargs):
        soup = BeautifulSoup(raw_data, 'lxml')
        soup.prettify()

        website_text = ""

        # Text within 'p' tags is retrieved
        for i in soup.find_all('p'):
            website_text += i.text + "\n\n"

        return website_text

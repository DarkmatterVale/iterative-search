import unittest
from ..data_processor import HTMLDataProcessor

class HTMLDataProcessorTestCase(unittest.TestCase):

    def test_process_html_pass(self):
        test_html = "<html><body><p>Some <b>bad <i>HTML</i></b></p></body></html>"

        processor = HTMLDataProcessor()
        processed_text = processor.process(test_html)

        self.assertEqual("Some bad HTML\n\n", processed_text)

    def test_process_html_pass_2(self):
        test_html = "<html><body><p>Some <b>bad <i>HTML</i></b></p><p>Some more <b>bad <i>HTML</i></b></p></body></html>"

        processor = HTMLDataProcessor()
        processed_text = processor.process(test_html)

        self.assertEqual("Some bad HTML\n\nSome more bad HTML\n\n", processed_text)

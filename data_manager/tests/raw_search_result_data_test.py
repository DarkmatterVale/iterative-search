import unittest
from ..model import RawSearchResultData

class RawSearchResultDataTestCase(unittest.TestCase):

    def test_construction_pass(self):
        data = RawSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_html")

        self.assertEqual(data.get_search_query(), "search_query")
        self.assertEqual(data.get_result_hyperlink(), "result_hyperlink")
        self.assertEqual(data.get_result_timestamp(), "result_timestamp")
        self.assertEqual(data.get_result_html(), "result_html")

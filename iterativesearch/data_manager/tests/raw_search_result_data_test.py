import unittest
from ..model import RawSearchResultData
from ..model import DataEntry

class RawSearchResultDataTestCase(unittest.TestCase):

    def test_construction_pass(self):
        data = RawSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_html")

        self.assertEqual(data.get_search_query(), "search_query")
        self.assertEqual(data.get_result_hyperlink(), "result_hyperlink")
        self.assertEqual(data.get_result_timestamp(), "result_timestamp")
        self.assertEqual(data.get_result_html(), "result_html")

    def test_from_data_entry_pass(self):
        data_entry = DataEntry(attributes = {
            "SEARCH_QUERY" : "search_query",
            "RESULT_HYPERLINK" : "result_hyperlink",
            "RESULT_TIMESTAMP_ATTR_KEY" : "result_timestamp",
            "RESULT_HTML" : "result_html"
        })

        converted_data = RawSearchResultData.from_data_entry(data_entry)

        self.assertEqual(converted_data.get_search_query(), "search_query")
        self.assertEqual(converted_data.get_result_hyperlink(), "result_hyperlink")
        self.assertEqual(converted_data.get_result_timestamp(), "result_timestamp")
        self.assertEqual(converted_data.get_result_html(), "result_html")

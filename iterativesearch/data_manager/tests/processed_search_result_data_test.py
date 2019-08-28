import unittest
from ..model import ProcessedSearchResultData
from ..model import DataEntry

class ProcessedSearchResultDataTestCase(unittest.TestCase):

    def test_construction_pass(self):
        data = ProcessedSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_text")

        self.assertEqual(data.get_search_query(), "search_query")
        self.assertEqual(data.get_result_hyperlink(), "result_hyperlink")
        self.assertEqual(data.get_result_timestamp(), "result_timestamp")
        self.assertEqual(data.get_result_text(), "result_text")

    def test_from_data_entry_pass(self):
        data_entry = DataEntry(attributes = {
            "SEARCH_QUERY" : "search_query",
            "RESULT_HYPERLINK" : "result_hyperlink",
            "RESULT_TIMESTAMP_ATTR_KEY" : "result_timestamp",
            "RESULT_TEXT" : "result_text"
        })

        converted_data = ProcessedSearchResultData.from_data_entry(data_entry)

        self.assertEqual(converted_data.get_search_query(), "search_query")
        self.assertEqual(converted_data.get_result_hyperlink(), "result_hyperlink")
        self.assertEqual(converted_data.get_result_timestamp(), "result_timestamp")
        self.assertEqual(converted_data.get_result_text(), "result_text")

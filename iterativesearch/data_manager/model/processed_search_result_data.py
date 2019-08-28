from .search_result_data import SearchResultData

class ProcessedSearchResultData(SearchResultData):

    RESULT_TEXT_ATTR_KEY = "RESULT_TEXT"

    def __init__(self, search_query, result_hyperlink, result_timestamp, text):
        super(ProcessedSearchResultData, self).__init__(search_query, result_hyperlink, result_timestamp)

        self.set_attribute(ProcessedSearchResultData.RESULT_TEXT_ATTR_KEY, text)

    def get_result_text(self):
        return self.get_attribute(ProcessedSearchResultData.RESULT_TEXT_ATTR_KEY)

    @staticmethod
    def from_data_entry(data_entry):
        return ProcessedSearchResultData(
            data_entry.get_attribute(SearchResultData.SEARCH_QUERY_ATTR_KEY),
            data_entry.get_attribute(SearchResultData.RESULT_HYPERLINK_ATTR_KEY),
            data_entry.get_attribute(SearchResultData.RESULT_TIMESTAMP_ATTR_KEY),
            data_entry.get_attribute(ProcessedSearchResultData.RESULT_TEXT_ATTR_KEY))

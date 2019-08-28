from .search_result_data import SearchResultData

class RawSearchResultData(SearchResultData):

    RESULT_HTML_ATTR_KEY = "RESULT_HTML"

    def __init__(self, search_query, result_hyperlink, result_timestamp, result_html):
        super(RawSearchResultData, self).__init__(search_query, result_hyperlink, result_timestamp)

        self.set_attribute(RawSearchResultData.RESULT_HTML_ATTR_KEY, result_html)

    def get_result_html(self):
        return self.get_attribute(RawSearchResultData.RESULT_HTML_ATTR_KEY)

    @staticmethod
    def from_data_entry(data_entry):
        return RawSearchResultData(
            data_entry.get_attribute(SearchResultData.SEARCH_QUERY_ATTR_KEY),
            data_entry.get_attribute(SearchResultData.RESULT_HYPERLINK_ATTR_KEY),
            data_entry.get_attribute(SearchResultData.RESULT_TIMESTAMP_ATTR_KEY),
            data_entry.get_attribute(RawSearchResultData.RESULT_HTML_ATTR_KEY))

from .data_entry import DataEntry

class RawSearchResultData(DataEntry):

    SEARCH_QUERY_ATTR_KEY = "SEARCH_QUERY"
    RESULT_HYPERLINK_ATTR_KEY = "RESULT_HYPERLINK"
    RESULT_TIMESTAMP_ATTR_KEY = "RESULT_TIMESTAMP_ATTR_KEY"
    RESULT_HTML_ATTR_KEY = "RESULT_HTML"

    def __init__(self, search_query, result_hyperlink, result_timestamp, result_html):
        super(RawSearchResultData, self).__init__(attributes={
            RawSearchResultData.SEARCH_QUERY_ATTR_KEY : search_query,
            RawSearchResultData.RESULT_HYPERLINK_ATTR_KEY : result_hyperlink,
            RawSearchResultData.RESULT_TIMESTAMP_ATTR_KEY : result_timestamp,
            RawSearchResultData.RESULT_HTML_ATTR_KEY : result_html
        })

    def get_search_query(self):
        return self.get_attribute(RawSearchResultData.SEARCH_QUERY_ATTR_KEY)

    def get_result_hyperlink(self):
        return self.get_attribute(RawSearchResultData.RESULT_HYPERLINK_ATTR_KEY)

    def get_result_timestamp(self):
        return self.get_attribute(RawSearchResultData.RESULT_TIMESTAMP_ATTR_KEY)

    def get_result_html(self):
        return self.get_attribute(RawSearchResultData.RESULT_HTML_ATTR_KEY)

from .data_entry import DataEntry

class SearchResultData(DataEntry):

    SEARCH_QUERY_ATTR_KEY = "SEARCH_QUERY"
    RESULT_HYPERLINK_ATTR_KEY = "RESULT_HYPERLINK"
    RESULT_TIMESTAMP_ATTR_KEY = "RESULT_TIMESTAMP_ATTR_KEY"

    def __init__(self, search_query, result_hyperlink, result_timestamp):
        super(SearchResultData, self).__init__(attributes={
            SearchResultData.SEARCH_QUERY_ATTR_KEY : search_query,
            SearchResultData.RESULT_HYPERLINK_ATTR_KEY : result_hyperlink,
            SearchResultData.RESULT_TIMESTAMP_ATTR_KEY : result_timestamp,
        })

    def get_search_query(self):
        return self.get_attribute(SearchResultData.SEARCH_QUERY_ATTR_KEY)

    def get_result_hyperlink(self):
        return self.get_attribute(SearchResultData.RESULT_HYPERLINK_ATTR_KEY)

    def get_result_timestamp(self):
        return self.get_attribute(SearchResultData.RESULT_TIMESTAMP_ATTR_KEY)

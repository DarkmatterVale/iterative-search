from abc import abstractmethod

class DataLake:

    @abstractmethod
    def initialize(self, **kwargs):
        """
        Handles all initialization. Should be used for one-time executions such as DB connections, etc.
        """
        raise NotImplementedError("initialize() not implemented")

    @abstractmethod
    def get_all_data(self):
        """
        Returns all data stored in the data lake.

        :return: list(RawSearchResultData)
        """
        raise NotImplementedError("get_all_data() not implemented")

    @abstractmethod
    def add_data(self, search_query_result_data):
        """
        Add a piece of data to the data lake.

        :param search_query_result_data: Search query result data
        :type search_query_result_data: RawSearchResultData
        """
        raise NotImplementedError("add_data() not implemented")

    @abstractmethod
    def query(self, query_parameters):
        """
        Queries the data lake using the query parameters object. Will return all results that satisfy the query.

        :param query_parameters: Query parameters.
        :type query_parameters: DataLakeQueryParameters
        :return: list(RawSearchResultData)
        """
        raise NotImplementedError("query() not implemented")

    @abstractmethod
    def clear_all_data(self):
        """
        Clear all data from the data lake.
        """
        raise NotImplementedError("clear_all_data() not implemented")

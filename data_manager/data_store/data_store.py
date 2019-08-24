from abc import abstractmethod

class DataStore:

    @abstractmethod
    def initialize(self, **kwargs):
        """
        Handles all initialization. Should be used for one-time executions such as DB connections, etc.
        """
        raise NotImplementedError("initialize() not implemented")

    @abstractmethod
    def get_all_data(self):
        """
        Returns all data stored in the data store.

        :return: list(DataEntry)
        """
        raise NotImplementedError("get_all_data() not implemented")

    @abstractmethod
    def add_data(self, data):
        """
        Add a piece of data to the data store.

        :param data: data
        :type data: DataEntry
        """
        raise NotImplementedError("add_data() not implemented")

    @abstractmethod
    def query(self, query_parameters):
        """
        Queries the data store using the query parameters object. Will return all results that satisfy the query.

        :param query_parameters: Query parameters.
        :type query_parameters: DataStoreQueryParameters
        :return: list(DataEntry)
        """
        raise NotImplementedError("query() not implemented")

    @abstractmethod
    def clear_all_data(self):
        """
        Clear all data from the data store.
        """
        raise NotImplementedError("clear_all_data() not implemented")

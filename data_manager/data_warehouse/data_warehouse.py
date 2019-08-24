from abc import abstractmethod

class DataWarehouse:

    @abstractmethod
    def initialize(self, **kwargs):
        """
        Handles all initialization. Should be used for one-time executions such as DB connections, etc.
        """
        raise NotImplementedError("initialize() not implemented")

    @abstractmethod
    def get_all_data(self):
        """
        Returns all data stored in the data warehouse.

        :return: list(ProcessedWarehouseData)
        """
        raise NotImplementedError("get_all_data() not implemented")

    @abstractmethod
    def add_data(self, processed_warehouse_data):
        """
        Add a piece of data to the data warehouse.

        :param processed_warehouse_data: Search query result data
        :type processed_warehouse_data: ProcessedWarehouseData
        """
        raise NotImplementedError("add_data() not implemented")

    @abstractmethod
    def query(self, query_parameters):
        """
        Queries the data warehouse using the query parameters object. Will return all results that satisfy the query.

        :param query_parameters: Query parameters.
        :type query_parameters: DataWarehouseQueryParameters
        :return: list(ProcessedWarehouseData)
        """
        raise NotImplementedError("query() not implemented")

    @abstractmethod
    def clear_all_data(self):
        """
        Clear all data from the data warehouse.
        """
        raise NotImplementedError("clear_all_data() not implemented")

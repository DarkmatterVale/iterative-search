from ..data_store import DataStore

class FlatFileDataStore(DataStore):

    def initialize(self, **kwargs):
        raise NotImplementedError("initialize() not implemented")

    def get_all_data(self):
        raise NotImplementedError("get_all_data() not implemented")

    def add_data(self, data):
        raise NotImplementedError("add_data() not implemented")

    def query(self, query_parameters):
        raise NotImplementedError("query() not implemented")

    def clear_all_data(self):
        raise NotImplementedError("clear_all_data() not implemented")

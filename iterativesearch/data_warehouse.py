from .data_manager import FlatFileDataStore
from .data_manager import ProcessedSearchResultData

class IterativeSearchDataWarehouse(FlatFileDataStore):

    def __init__(self, path="/iterative-search-data-warehouse"):
        super(IterativeSearchDataWarehouse, self).__init__(path)

    def get_all_data(self):
        data = super(IterativeSearchDataWarehouse, self).get_all_data()

        return [ProcessedSearchResultData.from_data_entry(data_entry) for data_entry in data]

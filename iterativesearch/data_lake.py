from .data_manager import FlatFileDataStore
from .data_manager import RawSearchResultData

class IterativeSearchDataLake(FlatFileDataStore):

    def __init__(self, path="/iterative-search-data-lake"):
        super(IterativeSearchDataLake, self).__init__(path)

    def get_all_data(self):
        data = super(IterativeSearchDataLake, self).get_all_data()

        return [RawSearchResultData.from_data_entry(data_entry) for data_entry in data]

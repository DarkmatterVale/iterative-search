from ..data_warehouse import IterativeSearchDataWarehouse
from ..data_manager import ProcessedSearchResultData
import unittest
import os
import shutil

class IterativeSearchDataWarehouseTestCase(unittest.TestCase):

    def tearDown(self):
        if os.path.exists("test_data_warehouse"):
            shutil.rmtree("test_data_warehouse")

    def test_get_all_data_pass(self):
        data_store = IterativeSearchDataWarehouse(path="test_data_warehouse")
        data_store.initialize()

        data1 = ProcessedSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_text")

        data_store.add_data(data1)

        data = data_store.get_all_data()

        self.assertEqual(1, len(data))
        self.assertEqual(ProcessedSearchResultData, type(data[0]))

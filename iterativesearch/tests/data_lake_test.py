from ..data_lake import IterativeSearchDataLake
from ..data_manager import RawSearchResultData
import unittest
import os
import shutil

class IterativeSearchDataLakeTestCase(unittest.TestCase):

    def tearDown(self):
        if os.path.exists("test_data_lake"):
            shutil.rmtree("test_data_lake")

    def test_get_all_data_pass(self):
        data_store = IterativeSearchDataLake(path="test_data_lake")
        data_store.initialize()

        data1 = RawSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_html")

        data_store.add_data(data1)

        data = data_store.get_all_data()

        self.assertEqual(1, len(data))
        self.assertEqual(RawSearchResultData, type(data[0]))

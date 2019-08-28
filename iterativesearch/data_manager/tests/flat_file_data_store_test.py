import unittest
import os
import shutil
from ..data_store import FlatFileDataStore
from ..model import RawSearchResultData

class FlatFileDataStoreTestCase(unittest.TestCase):

    def tearDown(self):
        if os.path.exists("test_data_store"):
            shutil.rmtree("test_data_store")

    def test_data_store_initialize_pass(self):
        data_store = FlatFileDataStore(path="test_data_store")

        self.assertFalse(os.path.exists("test_data_store"))

        data_store.initialize()

        self.assertTrue(os.path.exists("test_data_store"))

    def test_add_data_pass(self):
        data_store = FlatFileDataStore(path="test_data_store")
        data_store.initialize()

        data1 = RawSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_html")

        data_store.add_data(data1)

        self.assertEqual(len(os.listdir("test_data_store")), 1)

        data_store.add_data(data1)

        self.assertEqual(len(os.listdir("test_data_store")), 2)

        data_store.add_data(data1)

        self.assertEqual(len(os.listdir("test_data_store")), 3)

    def test_get_all_data_pass(self):
        data_store = FlatFileDataStore(path="test_data_store")
        data_store.initialize()

        data1 = RawSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_html")

        data_store.add_data(data1)

        data = data_store.get_all_data()

        self.assertEqual(1, len(data))

    def test_clear_all_data_pass(self):
        data_store = FlatFileDataStore(path="test_data_store")
        data_store.initialize()

        data1 = RawSearchResultData("search_query", "result_hyperlink", "result_timestamp", "result_html")

        data_store.add_data(data1)

        data_store.clear_all_data()

        self.assertEqual(len(os.listdir("test_data_store")), 0)

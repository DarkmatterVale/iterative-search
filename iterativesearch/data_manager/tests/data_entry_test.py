import unittest
from ..model import DataEntry

class DataEntryTestCase(unittest.TestCase):

    def test_to_json_pass(self):
        data_entry = DataEntry(attributes={"test1" : "val1", "test3" : "val3"})

        json_data = data_entry.to_json()

        self.assertTrue("test1" in json_data)
        self.assertTrue("test3" in json_data)

    def test_from_json_pass(self):
        data_entry = DataEntry(attributes={"test1" : "val1", "test3" : "val3"})

        json_data = data_entry.to_json()

        second_data_entry = DataEntry.from_json(json_data)

        self.assertEqual("val1", second_data_entry.get_attribute("test1"))
        self.assertEqual("val3", second_data_entry.get_attribute("test3"))

    def test_has_attribute_pass(self):
        data_entry = DataEntry(attributes={"test1" : "val1", "test3" : "val3"})

        self.assertTrue(data_entry.has_attribute("test1"))
        self.assertFalse(data_entry.has_attribute("test10"))

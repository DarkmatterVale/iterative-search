from ..google_search_engine import GoogleSearchEngine
import unittest
from loguru import logger

class GoogleTestCase(unittest.TestCase):

    def test_search_pass_1(self):
        google_obj = GoogleSearchEngine(logger)

        results = google_obj.search("what is 100*100?")

        self.assertTrue(len(results) > 0)

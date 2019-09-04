from .search_engine import SearchEngine
from googlesearch import search
import requests

class GoogleSearchEngine(SearchEngine):

    def __init__(self, logger):
        self.logger = logger

    def search(self, query):
        results = []

        # Searches google using input term
        # Results are added to list of urls
        try:
            for url in search(query, stop=50):
                source = requests.get(url).text
                results.append((url, source))
        except:
            self.logger.error("\nConnection timed out. Could not search Google")

        return results

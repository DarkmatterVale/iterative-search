from abc import abstractmethod

class SearchEngine:

    @abstractmethod
    def search(self, query):
        """
        Search the search engine with the given query.

        :param query: Query to search
        :type query: str
        :returns: list(BeautifulSoup)
        """
        raise NotImplementedError("search() not implemented")

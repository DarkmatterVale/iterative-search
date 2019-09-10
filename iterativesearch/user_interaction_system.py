from loguru import logger
from search_engine import GoogleSearchEngine
from data_manager.model import ProcessedSearchResultData
from data_manager.data_processor import HTMLDataProcessor

def isRelevant(sites):
    x = 0
    while x < len(sites):
        relevant = input('Is the website {} relevant to your search? Y or N :'.format(sites[x]))
        relevant.lower()
        if relevant[0] == 'n':
            sites.remove(sites[x])
        if relevant[0] == 'y':
            x += 1
        else:
            "Please enter Y or N"
    return sites

def get_results(search_engine, query):
    """
    :param search_engine: Search engine to use to execute query
    :type search_engine: SearchEngine
    :param query: Query to search
    :type query: str
    """
    return search_engine.search(query)

def execute_query(search_engine, data_processor, query):
    """
    :param search_engine: Search engine to use to execute query
    :type search_engine: SearchEngine
    :param data_processor: Processor used to convert raw results
    :type data_processor: DataProcessor
    :param query: Query to search
    :type query: str
    """
    results = get_results(search_engine, query)

    processed_results = []
    for result in results:
        processed_results.append(ProcessedSearchResultData(query, result[0], "TO DO", data_processor.process(result[1])))

    return processed_results

def main():
    google_search_engine = GoogleSearchEngine(logger)
    html_processor = HTMLDataProcessor()

    while True:
        query = input('Enter search query: ')

        processed_results = execute_query(google_search_engine, html_processor, query)

        for result in processed_results:
            print(str(result))

if __name__ == "__main__":
    main()

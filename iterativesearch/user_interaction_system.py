from loguru import logger
from search_engine import GoogleSearchEngine

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


def main():
    google_search_engine = GoogleSearchEngine(logger)

    query = input('Enter search query: ')
    list = (isRelevant(google_search_engine.search(query)))
    print(len(list))
    print(list)

if __name__ == "__main__":
    main()

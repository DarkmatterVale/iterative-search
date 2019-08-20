from googlesearch import search
from bs4 import BeautifulSoup
import requests

def getSites(term):
    # Creates array for storage of urls
    sites = []

    # Searches google using input term
    # Results are added to list of urls
    try:
        print("Loading", end = '')
        for url in search(term, stop=50):
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            sites.append((soup.title.text, url))
            print('.', end = '')

            # Semantic Analysis System utilized here when completed

        return sites
    except:
        print("\nThe connection has timed out, please try again later")
        exit()


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
    term = input('Enter search term, hit "enter" to begin search: ')
    list = (isRelevant(getSites(term)))
    print(len(list))
    print(list)


if __name__ == "__main__": main()


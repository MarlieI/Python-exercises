#! python3
# pypiSearch.py - Opens several search results from https://pypi.org
# using the command line arguments
# From C12 of Automate The Boring Stuff

import webbrowser
import requests
import bs4
import sys

# Download webpage
print('Googling...')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/90.0.4430.212 Safari/537.36'}
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]), headers=headers)

try:
    res.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')

# Retrieve search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

results = []
for link in linkElems:
    newLink = link.get('href')
    newLink = 'https://pypi.org' + newLink
    results.append(newLink)

# Open tabs for first five search results
numOpen = min(5, len(results))
for i in range(numOpen):
    webbrowser.open(results[i])


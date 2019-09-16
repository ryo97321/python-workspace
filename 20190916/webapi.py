import requests
import pprint
from bs4 import BeautifulSoup

url = 'https://cloud.feedly.com/v3/search/feeds'
params = {'query': 'game', 'count': 3}

r = requests.get(url, params=params)

# print(r.text)
# print(r.json())
pprint.pprint(r.json(), depth=4, compact=True)


# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.json())
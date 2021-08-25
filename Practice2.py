import requests
from bs4 import BeautifulSoup


r = requests.get('https://en.wikipedia.org/wiki/Sortition')

soup = BeautifulSoup(r.content, 'html.parser')
html = list(soup.children)[2]
with open('analysis.html', 'w', encoding='utf-8') as fl:
    fl.write(str(soup.prettify()))
import requests
import pprint

r = requests.get('https://en.wikipedia.org/wiki/Sortition')

pprint.pp(r.headers)


with open('request.html', 'wb') as fl:
    fl.write(r.content)
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/'

query = 'python'
exp_level = 'entry_level'
location = 'Bloomington'
radius = '5'
job_type = 'fulltime'
param = 'jobs?q=' + query + '&l=' + location + '&radius=' + radius + '&jt=' + job_type + '&explvl=' + exp_level

r = requests.get(url + param)

with open('test.html', 'w') as fl:
    fl.write(str(r.text))
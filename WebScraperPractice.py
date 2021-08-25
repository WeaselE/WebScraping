import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'

param = 'jobs/'

job = 'senior-python-developer-0.html'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

results = soup.find(id='ResultsContainer')
# print(results.prettify())

job_elements = results.find_all('div', class_='card-content')

for job_element in job_elements:
    title_element = job_element.find('h2', class_='title is-5')
    company_element = job_element.find('h3', class_='subtitle is-6 company')
    location_element = job_element.find('p', class_='location')
    # print(title_element.text.strip())
    # print(company_element.text.strip())
    # print(location_element.text.strip())
    # print()

# with open('MainPage.html', 'w') as fl:
#     fl.write(r.text)

python_jobs = results.find_all('h2', string=lambda text:'engineer' in text.lower())

python_job_elements = [h2_elements.parent.parent.parent for h2_elements in python_jobs]

for job_element in python_job_elements:
    title_element = job_element.find('h2', class_='title is-5')
    company_element = job_element.find('h3', class_='subtitle is-6 company')
    location_element = job_element.find('p', class_='location')
    links = job_element.find_all('a')[1]['href']
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(links)
    print()
    
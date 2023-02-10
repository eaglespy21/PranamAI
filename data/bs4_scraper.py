import requests
from bs4 import BeautifulSoup

URL = 'https://www.quora.com/topic/India'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("span", recursive=True)

print(job_elements)
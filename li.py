import requests
from bs4 import BeautifulSoup
import time

html = requests.get("https://www.linkedin.com/jobs/search/?keywords=Hays&location=Polska&locationId=pl%3A0").text

while True:
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    body = soup.find(class_="results-count-string")
    if str(body):
        print (body)
        break
    time.sleep(30)
    html = requests.get("https://www.linkedin.com/jobs/search/?keywords=Hays&location=Polska&locationId=pl%3A0").text
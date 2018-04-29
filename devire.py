from bs4 import BeautifulSoup
import requests
import re

d = {}

def devire_pl(name=""):
    try:
        page_response = requests.get('https://www.devire.pl/znajdz-prace/?strona=1&sort=published&direction=desc', timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('input')
        print(data)

    except:
        'bad'


print(devire_pl('IT'))

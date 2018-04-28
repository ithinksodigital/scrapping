from bs4 import BeautifulSoup
import requests
import re

p = {}


def pracuj_pl(link, name=''):
    try:
        page_response = requests.get(link, timeout=40).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='o__search_results_title_number')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)

        new_entry = {
            name: rm_str
        }

    except:

        new_entry = {
            name: "0"
        }

    p.update(new_entry)

def pracuj_scrap():
    pracuj_pl('https://www.pracuj.pl/praca/Hays%20Poland;en', name='Hays')
    pracuj_pl('https://www.pracuj.pl/praca/grafton;kw', name='Grafton')
    pracuj_pl('https://www.pracuj.pl/praca/HRK%20S.A.;en', name='HRK')
    pracuj_pl('https://www.pracuj.pl/praca/devire;en', name='Devire')
    pracuj_pl('https://www.pracuj.pl/praca/Manpower;en', name='Manpower')
    pracuj_pl('https://www.pracuj.pl/praca/Randstad%20Polska;en', name='Randstad')
    pracuj_pl('https://www.pracuj.pl/praca/antal;en', name='Antal')
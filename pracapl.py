from bs4 import BeautifulSoup
import requests
import re

pr = {}

def praca_pl(link, name=''):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='margin-bottom-20 padding-left-20')
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

    pr.update(new_entry)

def praca_scrap():
    praca_pl('https://www.praca.pl/s-devire.html?p=devire', name='Devire')
    praca_pl('https://www.praca.pl/s-manpower.html?p=manpower', name="Manpower")
    praca_pl('https://www.praca.pl/s-antal.html?p=antal', name='Antal')
    praca_pl('https://www.praca.pl/s-randstad.html?p=randstad', name='Randstad')
    praca_pl('https://www.praca.pl/s-grafton.html?p=grafton', name='Grafton')
    praca_pl('https://www.praca.pl/s-hrk.html?p=hrk', name='HRK')
    praca_pl('https://www.praca.pl/s-hays,poland,sp,z,o-o.html?p=Hays+Poland+Sp.++z+o.o.%2C+', name='Hays')
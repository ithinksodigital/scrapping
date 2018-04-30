from bs4 import BeautifulSoup
import requests
import re

i = {}
def infopraca_pl(link, name=''):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='list-title')
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

    i.update(new_entry)

def infopraca_scrap():
    infopraca_pl('https://www.infopraca.pl/praca?q=hays+poland&lc=', name='Hays')
    infopraca_pl('https://www.infopraca.pl/praca?q=grafton&lc=', name='Grafton')
    infopraca_pl('https://www.infopraca.pl/praca?q=randstad&lc=', name='Randstad')
    infopraca_pl('https://www.infopraca.pl/praca?q=antal&lc=', name='Antal')
    infopraca_pl('https://www.infopraca.pl/praca?q=manpower&lc=', name='Manpower')
    infopraca_pl('https://www.infopraca.pl/praca?q=devire&lc=', name='Devire')
    infopraca_pl('https://www.infopraca.pl/praca?q=hrk&lc=', name='HRK')
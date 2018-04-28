from bs4 import BeautifulSoup
import requests
import re

g = {}

def golden_line(link, name=''):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='count')
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

    g.update(new_entry)

def goldenline_scrap():
    golden_line('https://www.goldenline.pl/praca/szukaj?query=hays+poland', name='Hays')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=grafton', name='Grafton')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=randstad', name='Randstad')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=antal', name='Antal')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=manpower', name='Manpower')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=devire', name='Devire')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=hrk+sa' , name='HRK')
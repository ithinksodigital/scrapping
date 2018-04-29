from bs4 import BeautifulSoup
import requests
import re

e = {}


def experis_pl(link, name=''):
    try:
        page_response = requests.get( link, timeout=5 ).text
        page_content = BeautifulSoup( page_response, 'lxml' )
        data = page_content.find_all( class_='intro' )
        data_into_str = data[0].text.strip()
        rm_str = re.sub( '[^0-9]', '', data_into_str )
        int( rm_str )
        new_entry = {
            name: rm_str
        }

    except:

        new_entry = {
            name: 0
        }

    e.update(new_entry)

def experis_scrap():
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3012&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'IT')
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3011&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'Inżynieria')
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3006&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'Finanse')
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=1&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'Inne')


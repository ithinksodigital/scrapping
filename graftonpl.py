from bs4 import BeautifulSoup
import requests
import re

g = {}

def grafton_pl(string, name=""):
    try:
        page_response = requests.get('https://www.grafton.pl/pl/job-search?job_types=permanent-165', timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('a.%s > span' % string)
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)

        new_entry = {
            name: int(rm_str )
        }
    except:

        new_entry = {
            name: 0
        }

    g.update(new_entry)


def grafton_scrap():
    grafton_pl('it-komunikacja', 'IT & Telekomunikacja' )
    grafton_pl('finanse-bankowosc-ksiegowosc', 'Finanse, Bankowość & Księgowość')
    grafton_pl('hr-prawo-administracja ', 'HR, Prawo & Administracja' )
    grafton_pl('sprzedaz-marketing-logistyka ', 'Sprzedaż, Marketing & Logistyka')
    grafton_pl('farmacja-sprzet-medyczny ', 'Farmacja & Sprzęt Medyczny')
    grafton_pl('praca-tymczasowa-outsourcing ', 'Praca Tymczasowa & Outsourcing' )
    grafton_pl('miedzynarodowe-rekrutacja ', 'Międzynarodowe rekrutacje')
    grafton_pl('produkcja ', 'Produkcja')
    grafton_pl('absolwenci ', 'Absolwenci')
    grafton_pl('obsluga-klienta ', 'Obsługa Klienta')
    grafton_pl('inzynieria ', 'Inżynieria')
    grafton_pl('budownictwo-zarzadzanie-nieruchomosciami ', 'Budownictwo & Zarządzanie Nieruchomościami')
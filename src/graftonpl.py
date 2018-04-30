from bs4 import BeautifulSoup
import requests
import csv
import re
import os

g = []

def grafton_pl(string, name=""):
    try:
        page_response = requests.get('https://www.grafton.pl/pl/job-search?job_types=permanent-165', timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('a.%s > span' % string)
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)

        new_entry = {
            "company_name": "Grafton",
            "category": name,
            "offers" : int(rm_str)
        }
    except:

        new_entry = {
            "company_name": "Grafton",
            "category": name,
            "offers": "not received"
        }

    g.extend([new_entry])


def grafton_scrap():
    grafton_pl( 'it-komunikacja', 'IT & Telekomunikacja' )
    grafton_pl( 'finanse-bankowosc-ksiegowosc', 'Finanse, Bankowosc & Ksiegowosc' )
    grafton_pl( 'hr-prawo-administracja ', 'HR, Prawo & Administracja' )
    grafton_pl('sprzedaz-marketing-logistyka ', 'Sprzedaz, Marketing & Logistyka')
    grafton_pl('farmacja-sprzet-medyczny ', 'Farmacja & Sprzet Medyczny')
    grafton_pl('praca-tymczasowa-outsourcing ', 'Praca Tymczasowa & Outsourcing' )
    grafton_pl('miedzynarodowe-rekrutacja ', 'Miedzynarodowe rekrutacje')
    grafton_pl('produkcja ', 'Produkcja')
    grafton_pl('absolwenci ', 'Absolwenci')
    grafton_pl('obsluga-klienta ', 'Obsluga Klienta')
    grafton_pl('inzynieria ', 'Inzynieria')
    grafton_pl('budownictwo-zarzadzanie-nieruchomosciami ', 'Budownictwo & Zarzadzanie Nieruchomosciami')

def grafton_export():
    global g
    test = []

    for document in g:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove('export/grafton.csv')
        with open( 'export/grafton.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fields = ['category', 'offerts']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter = ';')
            writer.writeheader()
            writer.writerows( test )
    except:
        with open( 'export/grafton.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter = ';' )
            writer.writeheader()
            writer.writerows( test )

    g = []
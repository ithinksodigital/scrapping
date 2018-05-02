from bs4 import BeautifulSoup
import requests
import csv
import re
import os

g = []

def grafton_pl(string, name="", company_name=''):

    try:
        page_response = requests.get('https://www.grafton.pl/pl/job-search?job_types=permanent-165', timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('a.%s > span' % string)
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers" : int(rm_str)
        }
    except:

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers": "not received"
        }

    g.extend([new_entry])
    return company_name
    return g



def grafton_scrap():
    grafton_pl( 'it-komunikacja', 'IT & Telekomunikacja', 'Grafton')
    grafton_pl( 'finanse-bankowosc-ksiegowosc', 'Finanse, Bankowosc & Ksiegowosc', 'Grafton' )
    grafton_pl( 'hr-prawo-administracja ', 'HR, Prawo & Administracja', 'Grafton')
    grafton_pl('sprzedaz-marketing-logistyka ', 'Sprzedaz, Marketing & Logistyka', 'Grafton')
    grafton_pl('farmacja-sprzet-medyczny ', 'Farmacja & Sprzet Medyczny', 'Grafton')
    grafton_pl('praca-tymczasowa-outsourcing ', 'Praca Tymczasowa & Outsourcing' , 'Grafton')
    grafton_pl('miedzynarodowe-rekrutacja ', 'Miedzynarodowe rekrutacje', 'Grafton')
    grafton_pl('produkcja ', 'Produkcja', 'Grafton')
    grafton_pl('absolwenci ', 'Absolwenci', 'Grafton')
    grafton_pl('obsluga-klienta ', 'Obsluga Klienta', 'Grafton')
    grafton_pl('inzynieria ', 'Inzynieria', 'Grafton')
    grafton_pl('budownictwo-zarzadzanie-nieruchomosciami ', 'Budownictwo & Zarzadzanie Nieruchomosciami', 'Grafton')

def grafton_export(company_name):
    path = '/home/jobad/scrapping/export/{}.csv'.format( company_name )

    global g
    test = []

    for document in g:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( path )
        with open( path, 'w', newline='', encoding='utf-8') as csvfile:
            fields = ['category', 'offerts']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )
    except:
        with open(path, 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )

    g = []
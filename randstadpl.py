from bs4 import BeautifulSoup
import requests
import re
import os
import csv

ra = []

def randstad_pl(string, name="", company_name=''):
    try:
        page_response = requests.get('https://www.randstad.pl/znajdz-prace/s-%s' %string, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('span#ctl07_ctl05_NrOfJobsLabelTop')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers": int( rm_str )
        }
    except:

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers": "not received"
        }

    ra.extend( [new_entry] )
    return company_name
    return ra

def randstad_scrap():
    randstad_pl('produkcja/','produkcja', 'Randstad' )
    randstad_pl('it-administracja/', 'IT - administracja', 'Randstad')
    randstad_pl('it-rozwoj-oprogramowania', 'it - rozwoj oprogramowania', 'Randstad')
    randstad_pl('administracja-biurowa', 'administracja biurowa', 'Randstad')
    randstad_pl( 'badania-i-rozwoj', 'badania i rozwoj', 'Randstad' )
    randstad_pl( 'bankowosc', 'bankowosc', 'Randstad')
    randstad_pl( 'budownictwo', 'budownictwo' , 'Randstad')
    randstad_pl( 'call-center', 'call center', 'Randstad' )
    randstad_pl( 'doradztwo-konsulting', 'doradztwo/konsulting' , 'Randstad')
    randstad_pl( 'edukacja-szkolenia', 'edukacja/szkolenia' , 'Randstad')
    randstad_pl( 'finanse-ekonomia', 'finanse/ekonomia', 'Randstad' )
    randstad_pl( 'hotelarstwo-gastronomia-turystyka', 'hotelarstwo/gastronomia/turystyka' , 'Randstad')
    randstad_pl('human-resources-zasoby-ludzkie', 'human resources/zasoby ludzkie', 'Randstad')
    randstad_pl('inne', 'inne', 'Randstad')
    randstad_pl('inzynieria', 'inzynieria', 'Randstad')
    randstad_pl( 'magazyn', 'magazyn' , 'Randstad')
    randstad_pl( 'marketing', 'marketing' , 'Randstad')
    randstad_pl( 'nieruchomosci', 'nieruchomosci' , 'Randstad')
    randstad_pl( 'obsluga-klienta', 'obsluga klienta' , 'Randstad')
    randstad_pl( 'produkcja', 'produkcja' , 'Randstad')
    randstad_pl( 'reklama-grafika-kreacja-fotografia', 'reklama/grafika/kreacja/fotografia' , 'Randstad')
    randstad_pl( 'sprzedaz', 'sprzedaz' , 'Randstad')
    randstad_pl( 'transport-spedycja-logistyka', 'transport/spedycja/logistyka', 'Randstad')
    randstad_pl( 'ubezpieczenia', 'ubezpieczenia' , 'Randstad')
    randstad_pl( 'uslugi', 'uslugi' , 'Randstad')
    randstad_pl( 'zakupy', 'zakupy' , 'Randstad')
    randstad_pl( 'lancuch-dostaw', 'lancuch dostaw' , 'Randstad')


def randstad_export(company_name):
    path = '/home/jobad/scrapping/export/{}.csv'.format( company_name )

    global ra
    test = []

    for document in ra:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( path )
        with open( path, 'w', newline='', encoding='utf-8') as csvfile:
            fields = ['category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )
    except:
        with open( path, 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )

    ra = []

from bs4 import BeautifulSoup
import requests
import re
import os
import csv


e = []

def experis_pl(link, name='', company_name=''):
    try:
        page_response = requests.get( link, timeout=5 ).text
        page_content = BeautifulSoup( page_response, 'lxml' )
        data = page_content.find_all( class_='intro' )
        data_into_str = data[0].text.strip()
        rm_str = re.sub( '[^0-9]', '', data_into_str )
        int( rm_str )

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

    e.extend([new_entry] )
    return e
    return company_name

def experis_scrap():
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3012&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'IT', 'Experis')
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3011&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'Inżynieria', 'Experis')
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3006&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'Finanse', 'Experis')
    experis_pl('https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=1&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
               'Inne', 'Experis')


def experis_export(company_name):
    global e
    test = []

    for document in e:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( 'export/%s.csv' %company_name )
        with open( 'export/%s.csv' %company_name, 'w', newline='', encoding='utf-8') as csvfile:
            fields = ['category', 'offerts']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )
    except:
        with open( 'export/%s.csv' %company_name, 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )

    e = []

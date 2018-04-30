from bs4 import BeautifulSoup
import requests
import re
import csv
import os

h = []

def hrk_pl(link, name=''):
    try:
        page_response = requests.get('https://www.hrk.pl/pl/jobs?search=&region=All&specialization=%s' %link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('div.offers > h1')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)

        new_entry = {
            "company_name": "HRK",
            "category": name,
            "offers": int(rm_str)
        }
    except:

        new_entry = {
            "company_name": "HRK",
            "category": name,
            "offers": "not received"
        }

    h.extend( [new_entry] )

def hrk_scrap():
    hrk_pl('869', 'Financial Markets')
    hrk_pl('870', 'Energy')
    hrk_pl('871', 'Engineering & Manufacturing')
    hrk_pl('872', 'FMCG')
    hrk_pl('873', 'Human Resources')
    hrk_pl('874', 'ICT')
    hrk_pl('875', 'Legal')
    hrk_pl('876', 'Logistics & Purchasing')
    hrk_pl('877', 'Media')
    hrk_pl('879', 'Real Estate & Construction')
    hrk_pl('880', 'Retail')
    hrk_pl('881', 'Finance')
    hrk_pl('882','Professional Services')
    hrk_pl('883', 'Life Science')
    hrk_pl( '884', 'SSC/BPO' )
    hrk_pl( '12353', 'ITC' )

def hrk_export():
    global h
    test = []

    for document in h:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( 'export/hrk.csv' )
        with open( 'export/hrk.csv', 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['category', 'offerts']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )
    except:
        with open( 'export/hrk.csv', 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )

    h = []
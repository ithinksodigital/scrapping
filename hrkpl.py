from bs4 import BeautifulSoup
import requests
import re
import csv
import os

h = []

def hrk_pl(link, name='', company_name=''):
    try:
        page_response = requests.get('https://www.hrk.pl/pl/jobs?search=&region=All&specialization=%s' %link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('div.offers > h1')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers": int(rm_str)
        }
    except:

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers": "not received"
        }

    h.extend( [new_entry] )
    return h
    return company_name

def hrk_scrap():
    hrk_pl('869', 'Financial Markets', 'HRK')
    hrk_pl('870', 'Energy', 'HRK')
    hrk_pl('871', 'Engineering & Manufacturing', 'HRK')
    hrk_pl('872', 'FMCG', 'HRK')
    hrk_pl('873', 'Human Resources', 'HRK')
    hrk_pl('874', 'ICT', 'HRK')
    hrk_pl('875', 'Legal', 'HRK')
    hrk_pl('876', 'Logistics & Purchasing', 'HRK')
    hrk_pl('877', 'Media', 'HRK')
    hrk_pl('879', 'Real Estate & Construction', 'HRK')
    hrk_pl('880', 'Retail', 'HRK')
    hrk_pl('881', 'Finance', 'HRK')
    hrk_pl('882','Professional Services', 'HRK')
    hrk_pl('883', 'Life Science', 'HRK')
    hrk_pl( '884', 'SSC/BPO', 'HRK' )
    hrk_pl( '12353', 'ITC', 'HRK' )

def hrk_export(company_name):
    global h
    test = []
    path = '/home/jobad/scrapping/export/{}.csv'.format( company_name )

    for document in h:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( path )
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
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

    h = []
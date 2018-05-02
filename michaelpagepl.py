from bs4 import BeautifulSoup
import requests
import re
import os
import csv

mp = []

def michaelpage_pl(string, name="", company_name='Michael Page'):
    try:
        page_response = requests.get('https://www.michaelpage.pl/jobs/%s' %string, timeout=30).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('div.no-of-jobs > span')
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

    mp.extend( [new_entry] )
    return company_name
    return mp

def michaelpage_scrap():
    michaelpage_pl('banking-financial-services-insurance', 'Banking & Financial Services, Insurance', 'Michael Page' )
    michaelpage_pl('consultancy-strategy-change', 'Consultancy, Strategy & Change', 'Michael Page')
    michaelpage_pl('customer-service', 'Customer Service', 'Michael Page')
    michaelpage_pl('engineering-manufacturing', 'Engineering & Manufacturing', 'Michael Page')
    michaelpage_pl('executive-search', 'Executive Search', 'Michael Page')
    michaelpage_pl('healthcare-life-sciences', 'Healthcare & Life Sciences', 'Michael Page')
    michaelpage_pl('human-resources', 'Human Resources', 'Michael Page')
    michaelpage_pl('information-technology', 'Information Technology', 'Michael Page')
    michaelpage_pl('legal', 'Legal', 'Michael Page')
    michaelpage_pl('logistics', 'Logistics', 'Michael Page')
    michaelpage_pl('marketing-agency-digital', 'Marketing Agency Digital', 'Michael Page')
    michaelpage_pl('office-business-support', 'Office Business Support', 'Michael Page')
    michaelpage_pl('procurement-supply-chain', 'Procurement Supply Chain', 'Michael Page')
    michaelpage_pl('property-construction-facilities-management', ' Property Construction Facilities Management', 'Michael Page')
    michaelpage_pl('retail-fashion', 'Retail Fashion', 'Michael Page')
    michaelpage_pl( 'sales', 'Sales', 'Michael Page' )

def michaelpage_export(company_name):
    path = '/home/jobad/scrapping/export/{}.csv'.format( company_name )

    global mp
    test = []

    for document in mp:
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

    mp = []

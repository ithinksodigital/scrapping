from bs4 import BeautifulSoup
import requests
import re

h = {}

def hrk_pl(link, name=''):
    try:
        page_response = requests.get('https://www.hrk.pl/pl/jobs?search=&region=All&specialization=%s' %link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('div.offers > h1')
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

    h.update(new_entry)

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
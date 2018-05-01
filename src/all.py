from bs4 import BeautifulSoup
import requests
import re
import os
import csv

all = []

def all_antal_pl(link, name=''):
    try:
        page_response = requests.get( link, timeout=10 ).text
        page_content = BeautifulSoup( page_response, 'lxml' ).find( class_='header' ).find_next_sibling().text.strip()
        rm_str = re.sub( '[^0-9]', '', page_content )

        new_entry = {
            "company_name": "Antal",
            "category": name,
            "offers": int( rm_str )
        }
    except:

        new_entry = {
            "company_name": "Antal",
            "category": name,
            "offers": "not received"
        }

    all.extend( [new_entry] )

def all_experis_pl(link, name=''):
    try:
        page_response = requests.get( link, timeout=5 ).text
        page_content = BeautifulSoup( page_response, 'lxml' )
        data = page_content.find_all( class_='intro' )
        data_into_str = data[0].text.strip()
        rm_str = re.sub( '[^0-9]', '', data_into_str )
        int( rm_str )

        new_entry = {
            "company_name": "Experis",
            "category": name,
            "offers": int( rm_str )
        }
    except:

        new_entry = {
            "company_name": "Experis",
            "category": name,
            "offers": "not received"
        }

    all.extend([new_entry] )

def all_grafton_pl(string, name=""):
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

    all.extend([new_entry])

def all_hays_pl(link, name=''):
    try:
        page_response = requests.get(link, timeout=10).text
        page_content = BeautifulSoup(page_response, 'lxml').find_all(class_ = 'count')
        data_into_str = page_content[0].text.strip()

        new_entry = {
            "company_name": "Hays",
            "category": name,
            "offers": int( data_into_str )
        }
    except:

        new_entry = {
            "company_name": "Hays",
            "category": name,
            "offers": "not received"
        }

    all.extend( [new_entry] )

def all_hrk_pl(link, name=''):
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

    all.extend( [new_entry] )

def all_manpower_pl(link, name=''):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='intro')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)

        new_entry = {
            "company_name": "Manpower",
            "category": name,
            "offers": int( rm_str )
        }
    except:

        new_entry = {
            "company_name": "Manpowers",
            "category": name,
            "offers": "not received"
        }

    all.extend( [new_entry] )

def all_randstad_pl(string, name=""):
    try:
        page_response = requests.get('https://www.randstad.pl/znajdz-prace/s-%s' %string, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('span#ctl07_ctl05_NrOfJobsLabelTop')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)

        new_entry = {
            "company_name": "Randstad",
            "category": name,
            "offers": int( rm_str )
        }
    except:

        new_entry = {
            "company_name": "Randstad",
            "category": name,
            "offers": "not received"
        }

    all.extend( [new_entry] )

def scrap():
    all_randstad_pl( 'produkcja/', 'produkcja' )
    all_randstad_pl( 'it-administracja/', 'IT - administracja' )
    all_randstad_pl( 'it-rozwoj-oprogramowania', 'it - rozwoj oprogramowania' )
    all_randstad_pl( 'administracja-biurowa', 'administracja biurowa' )
    all_randstad_pl( 'badania-i-rozwoj', 'badania i rozwoj' )
    all_randstad_pl( 'bankowosc', 'bankowosc' )
    all_randstad_pl( 'budownictwo', 'budownictwo' )
    all_randstad_pl( 'call-center', 'call center' )
    all_randstad_pl( 'doradztwo-konsulting', 'doradztwo/konsulting' )
    all_randstad_pl( 'edukacja-szkolenia', 'edukacja/szkolenia' )
    all_randstad_pl( 'finanse-ekonomia', 'finanse/ekonomia' )
    all_randstad_pl( 'hotelarstwo-gastronomia-turystyka', 'hotelarstwo/gastronomia/turystyka' )
    all_randstad_pl( 'human-resources-zasoby-ludzkie', 'human resources/zasoby ludzkie' )
    all_randstad_pl( 'inne', 'inne' )
    all_randstad_pl( 'inzynieria', 'inzynieria' )
    all_randstad_pl( 'magazyn', 'magazyn' )
    all_randstad_pl( 'marketing', 'marketing' )
    all_randstad_pl( 'nieruchomosci', 'nieruchomosci' )
    all_randstad_pl( 'obsluga-klienta', 'obsluga klienta' )
    all_randstad_pl( 'produkcja', 'produkcja' )
    all_randstad_pl( 'reklama-grafika-kreacja-fotografia', 'reklama/grafika/kreacja/fotografia' )
    all_randstad_pl( 'sprzedaz', 'sprzedaz' )
    all_randstad_pl( 'transport-spedycja-logistyka', 'transport/spedycja/logistyka' )
    all_randstad_pl( 'ubezpieczenia', 'ubezpieczenia' )
    all_randstad_pl( 'uslugi', 'uslugi' )
    all_randstad_pl( 'zakupy', 'zakupy' )
    all_randstad_pl( 'lancuch-dostaw', 'lancuch dostaw' )
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3001&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Administracja /Sekretariat/ Tlumaczenia')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3002&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='AGD/ Sprzet elektryczny')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3003&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Architektura/ Budownictwo')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3004&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Energetyka/ Gazownictwo')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3005&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Farmacja/ Chemia/ Biologia')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3006&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Finanse/ Bankowosć/ Ubezpieczenia')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3007&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='FMCG')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3008&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Gospodarstwo Domowe, naprawy i drobne uslugi')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3009&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='HR/ Szkolenia/ Edukacja')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3010&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Instytucje sektora publicznego')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3011&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Inzynieria/ Konstrukcje/ Technologie')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3012&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='IT/ Telekomunikacja/ Internet')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3013&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Kadra zarzadzajaca')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3014&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Komputery/ Sprzet elektroniczny i optyczny')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3014&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Konsulting/ Audyt')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3016&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Kopalnie/ Przemysl wydobywczy')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3017&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Ksiegowosć')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3018hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Lotnictwo')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3019&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Marketing/ Reklama/ PR')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3020&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Maszyny io wyposazenie: instalacja i naprawy')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3021&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Media/ Sztuka/ Rozrywka')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3022&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Medycyna/ Opieka zdrowotna')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3023&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Nieruchomosci')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3024&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Obsluga klienta/ Call Center')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3025&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Ochrona osob i mienia')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3026&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Ochrona srodowiska')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3027&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Organizacje pozytku publicznego')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3028&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Pojazdy mechaniczne')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3029&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Pojazdy mechaniczne, czesci i akcesoria: sprzedaz i naprawy')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3030&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl hutniczny i metalurgiczny')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3031&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl lekki')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3032&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl papierniczy')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3033&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl stoczniowy i kolejowy')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3034&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Restauracje/ Hotele')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3035&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Rolnictwo/ Lesnictwo/ Rybolostwo')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3036&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Sprzedaz detaliczna')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3037&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Sprzedaz hurtowa')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3038&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Szklo/ Ceramika/ Wyroby mineralne')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3039&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Transport/ Logistyka')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3040&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Uslugi prawne')
    all_manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3041&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Uslugi wodociagowe, kanalizacyjne i gospodarka odpadami')
    all_hrk_pl( '869', 'Financial Markets' )
    all_hrk_pl( '870', 'Energy' )
    all_hrk_pl( '871', 'Engineering & Manufacturing' )
    all_hrk_pl( '872', 'FMCG' )
    all_hrk_pl( '873', 'Human Resources' )
    all_hrk_pl( '874', 'ICT' )
    all_hrk_pl( '875', 'Legal' )
    all_hrk_pl( '876', 'Logistics & Purchasing' )
    all_hrk_pl( '877', 'Media' )
    all_hrk_pl( '879', 'Real Estate & Construction' )
    all_hrk_pl( '880', 'Retail' )
    all_hrk_pl( '881', 'Finance' )
    all_hrk_pl( '882', 'Professional Services' )
    all_hrk_pl( '883', 'Life Science' )
    all_hrk_pl( '884', 'SSC/BPO' )
    all_hrk_pl( '12353', 'ITC' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Badania+i+Rozw%C3%B3j+%26+Nauka%22%5D%5B%22Badania+i+Rozw%C3%B3j+%26+Nauka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Badania i Rozwój & Nauka' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Bankowo%C5%9B%C4%87+%26+Us%C5%82ugi+Finansowe%22%5D%5B%22Bankowo%C5%9B%C4%87+%26+Us%C5%82ugi+Finansowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Bankowość & Usługi Finanoswe' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Budownictwo%22%5D%5B%22Budownictwo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Budownictwo' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Cz%C4%99%C5%9Bci+samochodowe%22%5D%5B%22Cz%C4%99%C5%9Bci+samochodowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Części samochodowe' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Edukacja+%26+Szkolenia%22%5D%5B%22Edukacja+%26+Szkolenia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Edukacja & Szkolenia' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Farmacja%22%5D%5B%22Farmacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Farmacja' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Hotelarstwo%2C+Turystyka%2C+Rozrywka%22%5D%5B%22Hotelarstwo%2C+Turystyka%2C+Rozrywka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Hotelarstwo, Turystyka, Rozrywka' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22In%C5%BCynieria%22%5D%5B%22In%C5%BCynieria%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Inżynieria' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Logistyka+%26+%C5%81a%C5%84cuch+Dostaw%22%5D%5B%22Logistyka+%26+%C5%81a%C5%84cuch+Dostaw%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Logistyka & Łańcuch Dostaw' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Lotnictwo+%26+Kosmonautyka%22%5D%5B%22Lotnictwo+%26+Kosmonautyka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Lotnictwo & Kosmonautyka' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Nieruchomo%C5%9Bci%22%5D%5B%22Nieruchomo%C5%9Bci%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Nieruchomości' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Prawo%22%5D%5B%22Prawo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Prawo' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Produkcja%22%5D%5B%22Produkcja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Produkcja' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xIndustry%5B%22Przemys%C5%82+energetyczny+i+wydobywczy%22%5D%5B%22Przemys%C5%82+energetyczny+i+wydobywczy%22%5D&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Przemysł energetyczny i wydobywczy' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Radio%2C+TV%2C+Myzyka+%26+Film%22%5D%5B%22Radio%2C+TV%2C+Myzyka+%26+Film%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Radio, TV, Muzyka & Film' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Reklama%2C+Media%2C+PR%22%5D%5B%22Reklama%2C+Media%2C+PR%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Reklama, Media, PR' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Rekrutacja%22%5D%5B%22Rekrutacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Rekrutacja' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Rolnictwo%2C+Rybo%C5%82%C3%B3wstwo%2C+Le%C5%9Bnictwo%22%5D%5B%22Rolnictwo%2C+Rybo%C5%82%C3%B3wstwo%2C+Le%C5%9Bnictwo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Rolnictwo, Rybołóstwo, Leśnictwo' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Sektor+rz%C4%85dowy+i+publiczny%22%5D%5B%22Sektor+rz%C4%85dowy+i+publiczny%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Sektor rządowy i publiczny' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Sprzeda%C5%BC+detaliczna+i+dobra+konsumpcyjne%22%5D%5B%22Sprzeda%C5%BC+detaliczna+i+dobra+konsumpcyjne%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Sprzedaż detaliczna i dobra konsumpcyjne' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22S%C5%82u%C5%BCba+Zdrowia%22%5D%5B%22S%C5%82u%C5%BCba+Zdrowia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Służba Zdrowia' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Technologia+%26+Us%C5%82ugi+internetowe%22%5D%5B%22Technologia+%26+Us%C5%82ugi+internetowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Technologia & Usługi internetowe' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Telekomunikacja%22%5D%5B%22Telekomunikacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Telekomunikacja' )
    all_hays_pl( 'https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Ubezpieczenia%22%5D%5B%22Ubezpieczenia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Ubezpieczenia' )
    all_grafton_pl( 'it-komunikacja', 'IT & Telekomunikacja' )
    all_grafton_pl( 'finanse-bankowosc-ksiegowosc', 'Finanse, Bankowosc & Ksiegowosc' )
    all_grafton_pl( 'hr-prawo-administracja ', 'HR, Prawo & Administracja' )
    all_grafton_pl( 'sprzedaz-marketing-logistyka ', 'Sprzedaz, Marketing & Logistyka' )
    all_grafton_pl( 'farmacja-sprzet-medyczny ', 'Farmacja & Sprzet Medyczny' )
    all_grafton_pl( 'praca-tymczasowa-outsourcing ', 'Praca Tymczasowa & Outsourcing' )
    all_grafton_pl( 'miedzynarodowe-rekrutacja ', 'Miedzynarodowe rekrutacje' )
    all_grafton_pl( 'produkcja ', 'Produkcja' )
    all_grafton_pl( 'absolwenci ', 'Absolwenci' )
    all_grafton_pl( 'obsluga-klienta ', 'Obsluga Klienta' )
    all_grafton_pl( 'inzynieria ', 'Inzynieria' )
    all_grafton_pl( 'budownictwo-zarzadzanie-nieruchomosciami ', 'Budownictwo & Zarzadzanie Nieruchomosciami' )
    all_experis_pl(
        'https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3012&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'IT' )
    all_experis_pl(
        'https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3011&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Inżynieria' )
    all_experis_pl(
        'https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3006&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Finanse' )
    all_experis_pl(
        'https://www.experis.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=1&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Inne' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Accountancy', 'Accontancy' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Actuaries', 'Actuaries' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Administration+Support', 'Administration Supoort' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Banking%2C+Financial+Services+%26+Investment',
              'Banking, Financial services & Investment' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Consulting', 'Consulting' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Design%2C+Construction', 'Design, Construction' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Engineering', 'Engineering' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Fashion', 'Fashion' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=General+Management%2C+Board', 'General Management, Board' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Health%2C+Safety%2C+Environment',
              'Health, Safety, Environment' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Human+Resources', 'Human Resources' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=IT+%26+Telecom+Technical', 'IT & Telecom Technical' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Law%2C+Legal', 'Law, Legal' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Logistics%2C+Suply+chain', 'Logistic, suply chain' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Media', 'Media' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Operations', 'Operations' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Procurement%2C+Purchasing', 'Procurement, Purchasing' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+.NET', 'Programista .NET' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Android', 'Programista Android' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+aplikacji+mobilnych',
              'Programista aplikacji mobilnych' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+ASP.net', 'Programista ASP.net' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+C%23', 'Programista C' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+C%2B%2B', 'Programista C ++' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Front-End', 'Programista Front-End' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+iOS', 'Programista iOS' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+JAVA', 'Programista JAVA' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+perl', 'Programista Perl' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+PHP', 'Programista PHP' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Python', 'Programista Python' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Programista+Rails', 'Programista Rails' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Public+Sector%2C+Education%2C+Health',
              'Public Sector, Education, Health' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=R%26D%2C+Clinical%2FHealthcare%2C+Pharma',
              'R&D, Clinical/Healthcare, Pharma' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Sales%2C+Marketing%2C+PR', 'Sales, Marketing, PR' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Telekomunikacja', 'Telekomunikacja' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Testowanie', 'Testownie' )
    all_antal_pl( 'https://antal.pl/oferty-pracy?s=&sid=&did=Training', 'Training' )
    all_antal_pl(
        'https://antal.pl/oferty-pracy?s=&sid=&did=Zarz%C4%85dzanie+IT&bid=&wid=&mid=&pid=&pr=50&maps=&lat=51.919438&lng=19.14513599999998',
        'Zarzadzanie IT' )

def export():
    global all
    test = []

    for document in all:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( 'export/all.csv' )
        with open( 'export/all.csv', 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['category', 'offerts']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )
    except:
        with open( 'export/all.csv', 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )

    all = []
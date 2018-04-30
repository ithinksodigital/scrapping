from bs4 import BeautifulSoup
import requests
import re
import os
import csv

m = []


def manpower_pl(link, name=''):
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

    m.extend( [new_entry] )

def manpower_scrap():
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3001&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Administracja /Sekretariat/ Tlumaczenia')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3002&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='AGD/ Sprzet elektryczny')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3003&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Architektura/ Budownictwo')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3004&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Energetyka/ Gazownictwo')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3005&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Farmacja/ Chemia/ Biologia')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3006&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Finanse/ Bankowosć/ Ubezpieczenia')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3007&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='FMCG')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3008&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Gospodarstwo Domowe, naprawy i drobne uslugi')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3009&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='HR/ Szkolenia/ Edukacja')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3010&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Instytucje sektora publicznego')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3011&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Inzynieria/ Konstrukcje/ Technologie')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3012&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='IT/ Telekomunikacja/ Internet')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3013&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Kadra zarzadzajaca')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3014&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Komputery/ Sprzet elektroniczny i optyczny')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3014&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Konsulting/ Audyt')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3016&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Kopalnie/ Przemysl wydobywczy')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3017&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Ksiegowosć')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3018hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Lotnictwo')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3019&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Marketing/ Reklama/ PR')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3020&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Maszyny io wyposazenie: instalacja i naprawy')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3021&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Media/ Sztuka/ Rozrywka')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3022&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Medycyna/ Opieka zdrowotna')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3023&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Nieruchomosci')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3024&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Obsluga klienta/ Call Center')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3025&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Ochrona osob i mienia')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3026&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Ochrona srodowiska')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3027&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Organizacje pozytku publicznego')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3028&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Pojazdy mechaniczne')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3029&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Pojazdy mechaniczne, czesci i akcesoria: sprzedaz i naprawy')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3030&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl hutniczny i metalurgiczny')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3031&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl lekki')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3032&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl papierniczy')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3033&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Przemysl stoczniowy i kolejowy')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3034&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Restauracje/ Hotele')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3035&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Rolnictwo/ Lesnictwo/ Rybolostwo')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3036&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Sprzedaz detaliczna')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3037&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Sprzedaz hurtowa')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3038&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Szklo/ Ceramika/ Wyroby mineralne')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3039&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Transport/ Logistyka')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3040&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Uslugi prawne')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3041&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        name='Uslugi wodociagowe, kanalizacyjne i gospodarka odpadami')

def manpower_export():
    global m
    test = []

    for document in m:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( 'export/manpower.csv' )
        with open( 'export/manpower.csv', 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['category', 'offerts']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )
    except:
        with open( 'export/manpower.csv', 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )

    m = []
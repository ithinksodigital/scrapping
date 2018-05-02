from bs4 import BeautifulSoup
import requests
import re
import os
import csv

m = []


def manpower_pl(link, name='', comapny_name=''):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='intro')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)

        new_entry = {
            "company_name": comapny_name,
            "category": name,
            "offers": int( rm_str )
        }
    except:

        new_entry = {
            "company_name": comapny_name,
            "category": name,
            "offers": "not received"
        }

    m.extend( [new_entry] )
    return m
    return company_name

def manpower_scrap():
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3001&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Administracja /Sekretariat/ Tlumaczenia', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3002&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'AGD/ Sprzet elektryczny', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3003&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Architektura/ Budownictwo', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3004&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Energetyka/ Gazownictwo', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3005&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Farmacja/ Chemia/ Biologia', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3006&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Finanse/ Bankowosć/ Ubezpieczenia', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3007&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'FMCG', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3008&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Gospodarstwo Domowe, naprawy i drobne uslugi', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3009&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'HR/ Szkolenia/ Edukacja', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3010&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Instytucje sektora publicznego', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3011&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Inzynieria/ Konstrukcje/ Technologie', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3012&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'IT/ Telekomunikacja/ Internet', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3013&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Kadra zarzadzajaca', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3014&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Komputery/ Sprzet elektroniczny i optyczny', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3014&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Konsulting/ Audyt', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3016&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Kopalnie/ Przemysl wydobywczy', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3017&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Ksiegowosć', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3018hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Lotnictwo', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3019&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Marketing/ Reklama/ PR', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3020&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Maszyny io wyposazenie: instalacja i naprawy', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3021&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Media/ Sztuka/ Rozrywka', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3022&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Medycyna/ Opieka zdrowotna', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3023&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Nieruchomosci', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3024&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Obsluga klienta/ Call Center', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3025&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Ochrona osob i mienia', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3026&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Ochrona srodowiska', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3027&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Organizacje pozytku publicznego', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3028&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Pojazdy mechaniczne', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3029&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Pojazdy mechaniczne, czesci i akcesoria: sprzedaz i naprawy', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3030&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Przemysl hutniczny i metalurgiczny', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3031&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Przemysl lekki', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3032&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Przemysl papierniczy', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3033&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
       'Przemysl stoczniowy i kolejowy', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3034&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Restauracje/ Hotele', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3035&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Rolnictwo/ Lesnictwo/ Rybolostwo', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3036&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Sprzedaz detaliczna', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3037&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Sprzedaz hurtowa', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3038&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Szklo/ Ceramika/ Wyroby mineralne', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3039&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Transport/ Logistyka', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3040&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Uslugi prawne', 'Manpower')
    manpower_pl(
        'https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3041&hrlink_location=&hrlink_type=&hrlink_submitSearch=1',
        'Uslugi wodociagowe, kanalizacyjne i gospodarka odpadami', 'Manpower')

def manpower_export(company_name):
    path = '/home/jobad/scrapping/export/{}.csv'.format( company_name )

    global m
    test = []

    for document in m:
        event_obj = {}
        event_obj['company_name'] = document['company_name']
        event_obj['category'] = document['category']
        event_obj['offers'] = document['offers']
        test.append( event_obj )

    try:
        os.remove( path)
        with open( path, 'w', newline='', encoding='utf-8') as csvfile:
            fields = ['category', 'offerts']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )
    except:
        with open( path, 'w', newline='', encoding='utf-8' ) as csvfile:
            fields = ['company_name', 'category', 'offers']
            writer = csv.DictWriter( csvfile, fieldnames=fields, delimiter=';' )
            writer.writeheader()
            writer.writerows( test )

    m = []
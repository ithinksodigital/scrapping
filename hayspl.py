from bs4 import BeautifulSoup
import requests
import os
import csv
ha = []


def hays_pl(link, name='', company_name=''):
    try:
        page_response = requests.get(link, timeout=10).text
        page_content = BeautifulSoup(page_response, 'lxml').find_all(class_ = 'count')
        data_into_str = page_content[0].text.strip()

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers": int( data_into_str )
        }
    except:

        new_entry = {
            "company_name": company_name,
            "category": name,
            "offers": "not received"
        }

    ha.extend( [new_entry] )
    return ha
    return company_name

def hays_scrap():
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Badania+i+Rozw%C3%B3j+%26+Nauka%22%5D%5B%22Badania+i+Rozw%C3%B3j+%26+Nauka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Badania i Rozwój & Nauka', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Bankowo%C5%9B%C4%87+%26+Us%C5%82ugi+Finansowe%22%5D%5B%22Bankowo%C5%9B%C4%87+%26+Us%C5%82ugi+Finansowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Bankowość & Usługi Finanoswe', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Budownictwo%22%5D%5B%22Budownictwo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Budownictwo', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Cz%C4%99%C5%9Bci+samochodowe%22%5D%5B%22Cz%C4%99%C5%9Bci+samochodowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Części samochodowe', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Edukacja+%26+Szkolenia%22%5D%5B%22Edukacja+%26+Szkolenia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Edukacja & Szkolenia', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Farmacja%22%5D%5B%22Farmacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Farmacja', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Hotelarstwo%2C+Turystyka%2C+Rozrywka%22%5D%5B%22Hotelarstwo%2C+Turystyka%2C+Rozrywka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Hotelarstwo, Turystyka, Rozrywka', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22In%C5%BCynieria%22%5D%5B%22In%C5%BCynieria%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Inżynieria', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Logistyka+%26+%C5%81a%C5%84cuch+Dostaw%22%5D%5B%22Logistyka+%26+%C5%81a%C5%84cuch+Dostaw%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Logistyka & Łańcuch Dostaw', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Lotnictwo+%26+Kosmonautyka%22%5D%5B%22Lotnictwo+%26+Kosmonautyka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Lotnictwo & Kosmonautyka', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Nieruchomo%C5%9Bci%22%5D%5B%22Nieruchomo%C5%9Bci%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Nieruchomości', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Prawo%22%5D%5B%22Prawo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Prawo', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Produkcja%22%5D%5B%22Produkcja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Produkcja', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xIndustry%5B%22Przemys%C5%82+energetyczny+i+wydobywczy%22%5D%5B%22Przemys%C5%82+energetyczny+i+wydobywczy%22%5D&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Przemysł energetyczny i wydobywczy', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Radio%2C+TV%2C+Myzyka+%26+Film%22%5D%5B%22Radio%2C+TV%2C+Myzyka+%26+Film%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Radio, TV, Muzyka & Film', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Reklama%2C+Media%2C+PR%22%5D%5B%22Reklama%2C+Media%2C+PR%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Reklama, Media, PR', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Rekrutacja%22%5D%5B%22Rekrutacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Rekrutacja', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Rolnictwo%2C+Rybo%C5%82%C3%B3wstwo%2C+Le%C5%9Bnictwo%22%5D%5B%22Rolnictwo%2C+Rybo%C5%82%C3%B3wstwo%2C+Le%C5%9Bnictwo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Rolnictwo, Rybołóstwo, Leśnictwo', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Sektor+rz%C4%85dowy+i+publiczny%22%5D%5B%22Sektor+rz%C4%85dowy+i+publiczny%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Sektor rządowy i publiczny', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Sprzeda%C5%BC+detaliczna+i+dobra+konsumpcyjne%22%5D%5B%22Sprzeda%C5%BC+detaliczna+i+dobra+konsumpcyjne%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Sprzedaż detaliczna i dobra konsumpcyjne', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22S%C5%82u%C5%BCba+Zdrowia%22%5D%5B%22S%C5%82u%C5%BCba+Zdrowia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Służba Zdrowia', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Technologia+%26+Us%C5%82ugi+internetowe%22%5D%5B%22Technologia+%26+Us%C5%82ugi+internetowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Technologia & Usługi internetowe', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Telekomunikacja%22%5D%5B%22Telekomunikacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Telekomunikacja', 'Hays')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Ubezpieczenia%22%5D%5B%22Ubezpieczenia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Ubezpieczenia', 'Hays')


def hays_export(company_name):
    path = '/home/jobad/scrapping/export/{}.csv'.format( company_name )

    global ha
    test = []

    for document in ha:
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

    ha = []
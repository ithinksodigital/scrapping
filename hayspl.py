from bs4 import BeautifulSoup
import requests

ha = {}


def hays_pl(link, name=''):
    try:
        page_response = requests.get(link, timeout=10).text
        page_content = BeautifulSoup(page_response, 'lxml').find_all(class_ = 'count')
        data_into_str = page_content[0].text.strip()
        new_entry = {
            name: int(data_into_str)
        }

    except:

        new_entry = {
            name: 0
        }

    ha.update(new_entry)

def hays_scrap():
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Badania+i+Rozw%C3%B3j+%26+Nauka%22%5D%5B%22Badania+i+Rozw%C3%B3j+%26+Nauka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Badania i Rozwój & Nauka')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Bankowo%C5%9B%C4%87+%26+Us%C5%82ugi+Finansowe%22%5D%5B%22Bankowo%C5%9B%C4%87+%26+Us%C5%82ugi+Finansowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Bankowość & Usługi Finanoswe')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Budownictwo%22%5D%5B%22Budownictwo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Budownictwo')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Cz%C4%99%C5%9Bci+samochodowe%22%5D%5B%22Cz%C4%99%C5%9Bci+samochodowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Części samochodowe')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Edukacja+%26+Szkolenia%22%5D%5B%22Edukacja+%26+Szkolenia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Edukacja & Szkolenia')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Farmacja%22%5D%5B%22Farmacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Farmacja')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Hotelarstwo%2C+Turystyka%2C+Rozrywka%22%5D%5B%22Hotelarstwo%2C+Turystyka%2C+Rozrywka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Hotelarstwo, Turystyka, Rozrywka')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22In%C5%BCynieria%22%5D%5B%22In%C5%BCynieria%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Inżynieria')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Logistyka+%26+%C5%81a%C5%84cuch+Dostaw%22%5D%5B%22Logistyka+%26+%C5%81a%C5%84cuch+Dostaw%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Logistyka & Łańcuch Dostaw')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Lotnictwo+%26+Kosmonautyka%22%5D%5B%22Lotnictwo+%26+Kosmonautyka%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Lotnictwo & Kosmonautyka')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Nieruchomo%C5%9Bci%22%5D%5B%22Nieruchomo%C5%9Bci%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Nieruchomości')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Prawo%22%5D%5B%22Prawo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Prawo')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Produkcja%22%5D%5B%22Produkcja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Produkcja')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xIndustry%5B%22Przemys%C5%82+energetyczny+i+wydobywczy%22%5D%5B%22Przemys%C5%82+energetyczny+i+wydobywczy%22%5D&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Przemysł energetyczny i wydobywczy')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Radio%2C+TV%2C+Myzyka+%26+Film%22%5D%5B%22Radio%2C+TV%2C+Myzyka+%26+Film%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Radio, TV, Muzyka & Film')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Reklama%2C+Media%2C+PR%22%5D%5B%22Reklama%2C+Media%2C+PR%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Reklama, Media, PR')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Rekrutacja%22%5D%5B%22Rekrutacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Rekrutacja')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Rolnictwo%2C+Rybo%C5%82%C3%B3wstwo%2C+Le%C5%9Bnictwo%22%5D%5B%22Rolnictwo%2C+Rybo%C5%82%C3%B3wstwo%2C+Le%C5%9Bnictwo%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Rolnictwo, Rybołóstwo, Leśnictwo')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Sektor+rz%C4%85dowy+i+publiczny%22%5D%5B%22Sektor+rz%C4%85dowy+i+publiczny%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Sektor rządowy i publiczny')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Sprzeda%C5%BC+detaliczna+i+dobra+konsumpcyjne%22%5D%5B%22Sprzeda%C5%BC+detaliczna+i+dobra+konsumpcyjne%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Sprzedaż detaliczna i dobra konsumpcyjne')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22S%C5%82u%C5%BCba+Zdrowia%22%5D%5B%22S%C5%82u%C5%BCba+Zdrowia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Służba Zdrowia')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Technologia+%26+Us%C5%82ugi+internetowe%22%5D%5B%22Technologia+%26+Us%C5%82ugi+internetowe%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Technologia & Usługi internetowe')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Telekomunikacja%22%5D%5B%22Telekomunikacja%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Telekomunikacja')
    hays_pl('https://m.hays.pl/search/?q=hays&f=xjobType%5B%22P%22%5D%5B%22Sta%C5%82a%22%5D&f=xIndustry%5B%22Ubezpieczenia%22%5D%5B%22Ubezpieczenia%22%5D&locationLevel=&location=&locationSet=&locationId=',
            'Ubezpieczenia')
from bs4 import BeautifulSoup
import requests
import re

ra = {}

def randstad_pl(string, name=""):
    try:
        page_response = requests.get('https://www.randstad.pl/znajdz-prace/s-%s' %string, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.select('span#ctl07_ctl05_NrOfJobsLabelTop')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)

        new_entry = {
            name: int(rm_str )
        }
    except:

        new_entry = {
            name: 0
        }

    ra.update(new_entry)

def randstad_scrap():
    randstad_pl('produkcja/','produkcja' )
    randstad_pl('it-administracja/', 'IT - administracja')
    randstad_pl('it-rozwoj-oprogramowania', 'it - rozwoj oprogramowania')
    randstad_pl('administracja-biurowa', 'administracja biurowa')
    randstad_pl( 'badania-i-rozwoj', 'badania i rozwoj' )
    randstad_pl( 'bankowosc', 'bankowosc' )
    randstad_pl( 'budownictwo', 'budownictwo' )
    randstad_pl( 'call-center', 'call center' )
    randstad_pl( 'doradztwo-konsulting', 'doradztwo/konsulting' )
    randstad_pl( 'edukacja-szkolenia', 'edukacja/szkolenia' )
    randstad_pl( 'finanse-ekonomia', 'finanse/ekonomia' )
    randstad_pl( 'hotelarstwo-gastronomia-turystyka', 'hotelarstwo/gastronomia/turystyka' )
    randstad_pl('human-resources-zasoby-ludzkie', 'human resources/zasoby ludzkie')
    randstad_pl('inne', 'inne')
    randstad_pl('inzynieria', 'inzynieria')
    randstad_pl( 'magazyn', 'magazyn' )
    randstad_pl( 'marketing', 'marketing' )
    randstad_pl( 'nieruchomosci', 'nieruchomosci' )
    randstad_pl( 'obsluga-klienta', 'obsluga klienta' )
    randstad_pl( 'produkcja', 'produkcja' )
    randstad_pl( 'reklama-grafika-kreacja-fotografia', 'reklama/grafika/kreacja/fotografia' )
    randstad_pl( 'sprzedaz', 'sprzedaz' )
    randstad_pl( 'transport-spedycja-logistyka', 'transport/spedycja/logistyka')
    randstad_pl( 'ubezpieczenia', 'ubezpieczenia' )
    randstad_pl( 'uslugi', 'uslugi' )
    randstad_pl( 'zakupy', 'zakupy' )
    randstad_pl( 'lancuch-dostaw', 'lancuch dostaw' )




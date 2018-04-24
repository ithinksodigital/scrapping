from bs4 import BeautifulSoup
import requests
import re


def pracuj_pl(link):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='o__search_results_title_number')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)
        print('Pracuj.pl: ' + rm_str)
    except:
        print('Sorry, timeout. ')


def praca_pl(link):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='margin-bottom-20 padding-left-20')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)
        print('Praca.pl: ' + rm_str)
    except:
        print('Sorry, timeout. ')


def golden_line(link):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='count')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)
        print('GoldenLine: ' + rm_str)
    except:
        print('Sorry, timeout. ')


def infopraca_pl(link):
    try:
        page_response = requests.get(link, timeout=5).text
        page_content = BeautifulSoup(page_response, 'lxml')
        data = page_content.find_all(class_='list-title')
        data_into_str = data[0].text.strip()
        rm_str = re.sub('[^0-9]', '', data_into_str)
        int(rm_str)
        print('InfoPraca: ' + rm_str)
    except:
        print('Sorry, timeout. ')

print('''Hays
''')
pracuj_pl('https://www.pracuj.pl/praca/Hays%20Poland;en')
praca_pl('https://www.praca.pl/s-hays,poland,sp,z,o-o.html?p=Hays+Poland+Sp.++z+o.o.%2C+')
golden_line('https://www.goldenline.pl/praca/szukaj?query=hays+poland')
infopraca_pl('https://www.infopraca.pl/praca?q=hays+poland&lc=')
print('''-------
''')
print('''Grafton
''')
pracuj_pl('https://www.pracuj.pl/praca/grafton;kw')
praca_pl('https://www.praca.pl/s-grafton.html?p=grafton')
golden_line('https://www.goldenline.pl/praca/szukaj?query=grafton')
infopraca_pl('https://www.infopraca.pl/praca?q=grafton&lc=')
print('''-------
''')
print('''Randstad
''')
pracuj_pl('https://www.pracuj.pl/praca/Randstad%20Polska;en')
praca_pl('https://www.praca.pl/s-randstad.html?p=randstad')
golden_line('https://www.goldenline.pl/praca/szukaj?query=randstad')
infopraca_pl('https://www.infopraca.pl/praca?q=randstad&lc=')
print('''-------
''')
print('''Antal
''')

pracuj_pl('https://www.pracuj.pl/praca/antal;en')
praca_pl('https://www.praca.pl/s-antal.html?p=antal')
golden_line('https://www.goldenline.pl/praca/szukaj?query=antal')
infopraca_pl('https://www.infopraca.pl/praca?q=antal&lc=')
print('''-------
''')
print('''Manpower
''')
pracuj_pl('https://www.pracuj.pl/praca/Manpower;en')
praca_pl('https://www.praca.pl/s-manpower.html?p=manpower')
golden_line('https://www.goldenline.pl/praca/szukaj?query=manpower')
infopraca_pl('https://www.infopraca.pl/praca?q=manpower&lc=')
print('''-------
''')
print('''Devire
''')
pracuj_pl('https://www.pracuj.pl/praca/devire;en')
praca_pl('https://www.praca.pl/s-devire.html?p=devire')
golden_line('https://www.goldenline.pl/praca/szukaj?query=devire')
infopraca_pl('https://www.infopraca.pl/praca?q=devire&lc=')
print('''-------
''')
print('''HRK S.A
''')
pracuj_pl('https://www.pracuj.pl/praca/HRK%20S.A.;en')
praca_pl('https://www.praca.pl/s-hrk.html?p=hrk')
golden_line('https://www.goldenline.pl/praca/szukaj?query=hrk+sa')
infopraca_pl('https://www.infopraca.pl/praca?q=hrk&lc=')

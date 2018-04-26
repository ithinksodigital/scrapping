from bs4 import BeautifulSoup
import requests
import re
from flask import Flask, jsonify, render_template


app = Flask(__name__)

d = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pracuj')
def pracuj():
    def pracuj_pl(link, name=''):
        try:
            page_response = requests.get(link, timeout=1).text
            page_content = BeautifulSoup(page_response, 'lxml')
            data = page_content.find_all(class_='o__search_results_title_number')
            data_into_str = data[0].text.strip()
            rm_str = re.sub('[^0-9]', '', data_into_str)
            int(rm_str)
            new_entry = {
                name : rm_str
            }

        except TimeoutError:
            print('Sorry, timeout. ')

        d.update(new_entry)

    pracuj_pl('https://www.pracuj.pl/praca/Hays%20Poland;en', name = 'Hays')
    pracuj_pl('https://www.pracuj.pl/praca/grafton;kw', name='Grafton')
    pracuj_pl('https://www.pracuj.pl/praca/HRK%20S.A.;en', name='HRK')
    pracuj_pl('https://www.pracuj.pl/praca/devire;en', name='Devire')
    pracuj_pl('https://www.pracuj.pl/praca/Manpower;en', name='Manpower')
    pracuj_pl('https://www.pracuj.pl/praca/Randstad%20Polska;en', name='Randstad')
    pracuj_pl('https://www.pracuj.pl/praca/antal;en', name='Antal')

    return jsonify(d)


@app.route('/praca')
def praca():
    def praca_pl(link, name=''):
        try:
            page_response = requests.get(link, timeout=5).text
            page_content = BeautifulSoup(page_response, 'lxml')
            data = page_content.find_all(class_='margin-bottom-20 padding-left-20')
            data_into_str = data[0].text.strip()
            rm_str = re.sub('[^0-9]', '', data_into_str)
            int(rm_str)
            new_entry = {
                name : rm_str
            }

        except:
            new_entry = {
                name : "0"
            }

        d.update(new_entry)


    praca_pl('https://www.praca.pl/s-devire.html?p=devire', name='Devire')
    praca_pl('https://www.praca.pl/s-manpower.html?p=manpower', name="Manpower")
    praca_pl('https://www.praca.pl/s-antal.html?p=antal', name='Antal')
    praca_pl('https://www.praca.pl/s-randstad.html?p=randstad', name='Randstad')
    praca_pl('https://www.praca.pl/s-grafton.html?p=grafton', name='Grafton')
    praca_pl('https://www.praca.pl/s-hrk.html?p=hrk')
    praca_pl('https://www.praca.pl/s-hays,poland,sp,z,o-o.html?p=Hays+Poland+Sp.++z+o.o.%2C+', name='Hays')

    return jsonify(d)


@app.route('/goldenline')
def goldenline():
    def golden_line(link, name=''):
        try:
            page_response = requests.get(link, timeout=5).text
            page_content = BeautifulSoup(page_response, 'lxml')
            data = page_content.find_all(class_='count')
            data_into_str = data[0].text.strip()
            rm_str = re.sub('[^0-9]', '', data_into_str)
            int(rm_str)
            new_entry = {
                name : rm_str
            }

        except:
            new_entry = {
                name : "0"
            }

        d.update(new_entry)

    golden_line('https://www.goldenline.pl/praca/szukaj?query=hays+poland', name='Hays')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=grafton', name='Grafton')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=randstad', name='Randstad')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=antal', name='Antal')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=manpower', name='Manpower')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=devire', name='Devire')
    golden_line('https://www.goldenline.pl/praca/szukaj?query=hrk+sa' , name='HRK')

    return jsonify(d)

@app.route('/infopraca')
def infopraca():
    def infopraca_pl(link, name=''):
        try:
            page_response = requests.get(link, timeout=5).text
            page_content = BeautifulSoup(page_response, 'lxml')
            data = page_content.find_all(class_='list-title')
            data_into_str = data[0].text.strip()
            rm_str = re.sub('[^0-9]', '', data_into_str)
            int(rm_str)
            new_entry = {
                name : rm_str
            }

        except:
            new_entry = {
                name : "0"
            }

        d.update(new_entry)


    infopraca_pl('https://www.infopraca.pl/praca?q=hays+poland&lc=', name='Hays')
    infopraca_pl('https://www.infopraca.pl/praca?q=grafton&lc=', name='Grafton')
    infopraca_pl('https://www.infopraca.pl/praca?q=randstad&lc=', name='Randstad')
    infopraca_pl('https://www.infopraca.pl/praca?q=antal&lc=', name='Antal')
    infopraca_pl('https://www.infopraca.pl/praca?q=manpower&lc=', name='Manpower')
    infopraca_pl('https://www.infopraca.pl/praca?q=devire&lc=', name='Devire')
    infopraca_pl('https://www.infopraca.pl/praca?q=hrk&lc=', name='HRK')

    return jsonify(d)


@app.route('/manpower')
def manpower():
    def manpower_pl(link, name=''):
        try:
            page_response = requests.get(link, timeout=5).text
            page_content = BeautifulSoup(page_response, 'lxml')
            data = page_content.find_all(class_='intro')
            data_into_str = data[0].text.strip()
            rm_str = re.sub('[^0-9]', '', data_into_str)
            int(rm_str)
            new_entry = {
                name : rm_str
            }

        except:
            new_entry = {
                name : "0"
            }

        d.update(new_entry)

    manpower_pl('https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3001&hrlink_location=&hrlink_type=&hrlink_submitSearch=1', name='Administracja /Sekretariat/ Tlumaczenia')
    manpower_pl('https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3003&hrlink_location=&hrlink_type=&hrlink_submitSearch=1', name='Architektura/ Budownictwo')
    manpower_pl('https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3002&hrlink_location=&hrlink_type=&hrlink_submitSearch=1', name='AGD')
    manpower_pl('https://www.manpower.pl/szukaj-pracy/oferty-pracy/?hrlink_query=&hrlink_category=3004&hrlink_location=&hrlink_type=&hrlink_submitSearch=1', name='Energetyka/Gazownictwo')
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)

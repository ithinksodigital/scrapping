import sys
from flask import Flask, jsonify, render_template, send_file, request
from pracapl import *
from infopracapl import *
from goldenlinepl import *
from manpower import *
from antalpl import *
from graftonpl import *
from pracujpl import *
from randstadpl import *
from hrkpl import *
from hayspl import *
from experispl import *
from michaelpagepl import *


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pracuj')
def pracuj():
    pracuj_scrap()
    return jsonify(p)

@app.route('/praca')
def praca():
    praca_scrap()
    return jsonify(pr)


@app.route('/goldenline')
def goldenline():
    goldenline_scrap()
    return jsonify(g)

@app.route('/infopraca')
def infopraca():
    infopraca_scrap()

    return jsonify(i)

@app.route('/michaelpage')
def michaelpage():
    company_name='Michael Page'
    michaelpage_scrap()
    michaelpage_export('Michael Page')
    return render_template( 'company.html', data=mp, company_name=company_name )


@app.route('/manpower')
def manpower():
    company_name = "Manpower"
    manpower_scrap()
    manpower_export('Manpower')
    return render_template('company.html', data=m, company_name=company_name)

@app.route('/experis')
def experis():
    company_name = 'Experis'
    experis_scrap()
    experis_export("Experis")
    return render_template('company.html', data=e, company_name=company_name)


@app.route('/antal')
def antal():
    company_name='Antal'
    antal_scrap()
    antal_export('Antal')
    return render_template('company.html', data=a, company_name=company_name)

@app.route('/grafton')
def grafton():
    company_name='Grafton'
    grafton_scrap()
    grafton_export('Grafton')
    return render_template('company.html', data=g, company_name=company_name)

@app.route('/randstad')
def randstad():
    company_name='Randstad'
    randstad_scrap()
    randstad_export('Randstad')
    return render_template('company.html', data=ra, company_name=company_name)

@app.route('/hrk')
def hrk():
    company_name = 'HRK'
    hrk_scrap()
    hrk_export('HRK')
    return render_template('company.html', data=h, company_name=company_name)

@app.route('/hays')
def hays():

    company_name='Hays'
    hays_scrap()
    hays_export('Hays')
    return render_template('company.html', data=ha, company_name=company_name)


@app.route('/getCSV', methods=['GET'])
def plot_csv():
    company_name = request.args.get( 'company_name' )
    path = '/home/jobad/scrapping/export/{}.csv'.format( company_name )
    return send_file(path,
                     mimetype='text/csv',
                     attachment_filename='%s.csv' %company_name,
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

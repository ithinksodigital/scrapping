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


@app.route('/manpower')
def manpower():
    manpower_scrap()
    manpower_export()
    return jsonify(m)

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
    antal_export()
    return render_template('company.html', data=a, company_name=company_name)

@app.route('/grafton')
def grafton():
    grafton_scrap()
    grafton_export()
    return jsonify(g)

@app.route('/randstad')
def randstad():
    randstad_scrap()
    randstad_export()
    return jsonify(ra)

@app.route('/hrk')
def hrk():
    hrk_scrap()
    hrk_export()
    return jsonify(h)

@app.route('/hays')
def hays():
    hays_scrap()
    hays_export()
    return jsonify(ha)


@app.route('/getCSV', methods=['GET'])
def plot_csv():
    company_name = request.args.get( 'company_name' )
    return send_file('export/%s.csv' %company_name,
                     mimetype='text/csv',
                     attachment_filename='%s.csv' %company_name,
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

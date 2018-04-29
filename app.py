from flask import Flask, jsonify, render_template
from pracujpl import *
from pracapl import *
from infopracapl import *
from goldenlinepl import *
from manpower import *
from antalpl import *
from graftonpl import *
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
    return jsonify(m)

@app.route('/experis')
def experis():
    experis_scrap()
    return jsonify(e)


@app.route('/antal')
def antal():
    antal_scrap()
    return jsonify(a)

@app.route('/grafton')
def gratfon():
    grafton_scrap()
    return jsonify(g)

@app.route('/randstad')
def randstad():
    randstad_scrap()
    return jsonify(ra)

@app.route('/hrk')
def hrk():
    hrk_scrap()
    return jsonify(h)

@app.route('/hays')
def hays():
    hays_scrap()
    return jsonify(ha)

if __name__ == '__main__':
    app.run(debug=True)

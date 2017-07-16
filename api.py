#!/usr/bin/exn python
# Microservice to list source/destination alloved for currency exchange
# Version 0.1
# Author: Paolo M.
# Dependecies: pip install flask requests
# Listen on port 8080

from __future__ import print_function
from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect
app = Flask(__name__)

source_list = [{"name": "United Kingdom", "isoCode": "GB"}, {
    "name": "Ireland", "isoCode": "IE"}, {"name": "Italy", "isoCode": "IT"}]
destination_list = [{"name": "Spain", "isoCode": "ES"}, {
    "name": "France", "isoCode": "FR"}, {"name": "Germany", "isoCode": "DE"}]


@app.route("/")
def hello():
    return "Please use http://localhost:8080/v1/countries?target=&lt;source|destination&gt;<p>To get the list of available countries"


@app.route("/v1/countries")
def countries():
    args = request.args
    print(args)
    if args['target'] == 'source':
        return jsonify(source_list)
    if args['target'] == 'destination':
        return jsonify(destination_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

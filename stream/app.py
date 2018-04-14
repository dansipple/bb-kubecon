#!/usr/bin/python

import requests
import json

from flask import Flask, request

# stream listens to a set of HTTP posts

app = Flask(__name__)

@app.route('/get-quotes')
def get_quotes():
    return foo

@app.route('/add-quotes/', methods=['POST'])
def add_quotes():
    foo = request.form.get('tweet')
    print('hello',foo)
    return request.data

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

#!/usr/bin/python

import requests
import datetime
import json

from flask import Flask, request, jsonify

# stream listens to a set of HTTP posts

app = Flask(__name__)

quote = { 'author': 'Albert Einstein', 'created_at': '2012-04-05', 'text': 'Imagine is more important than knowledge.'}
quote2 = { 'author': 'Albert Einstein', 'created_at': '2012-04-05', 'text': 'Imagine is more important than knowledgs.'}

tweets = [quote, quote2]

@app.route('/get-quotes')
def get_quotes():
    return jsonify(tweets)

@app.route('/add-quotes/', methods=['POST'])
def add_quotes():
    foo = request.get_json()
    print('hello',foo)
    return "Received"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

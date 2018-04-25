#!/usr/bin/python

import requests
import datetime
import json
import sqlite3
import os
import logging

from flask import Flask, request, jsonify

# stream listens to a set of HTTP posts

app = Flask(__name__)

@app.route('/get-quotes/')
def get_quotes():
    conn = sqlite3.connect('tweet.db')
    c = conn.cursor()

    c.execute('select author, created_at, text from tweets order by created_at desc limit 4')
    rows = c.fetchall()
    
    tweets = [ ]

    for row in rows:
        tweet = { }
        tweet['author'] = row[0]
        tweet['created_at'] = row[1]
        tweet['text'] = row[2]
        tweets.append(tweet)

    return jsonify(tweets)

@app.route('/add-quotes/', methods=['POST'])
def add_quotes():
    tweet = request.get_json()
    # tweet = gdpr_filter(tweet)
    

    if os.path.exists('tweet.db')==False:
        init()

    author = tweet['author']
    created_at = tweet['created_at']
    quote = tweet['text']

    conn = sqlite3.connect('tweet.db')
    c = conn.cursor()
    c.execute('INSERT INTO tweets VALUES(?, ?, ?)',
             (author, created_at, quote))
    conn.commit()
    logging.info('Saved tweet', tweet)
    conn.close()

    return "Received"

def gdpr_filter(tweet):
    tweet['author'] = 'Anonymous'
    time.sleep(0.5)
    return tweet

def init():
    conn = sqlite3.connect('tweet.db')
    c = conn.cursor()
    c.execute('CREATE TABLE tweets (author text, created_at text, text text)')
    conn.close()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

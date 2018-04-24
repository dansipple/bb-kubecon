#!/usr/bin/python

import time
import requests
import json, os
import datetime

# Infinite loop; we can use `kubectl scale` to turn this on and off

url = 'http://35.195.162.45/stream/add-quotes/'
# url = 'http://localhost:8080/add-quotes/`

def main():

    with open('quotes.json') as json_file:
        json_data = json.load(json_file)

    while True:
        tweet = { }

        for quote in json_data:
            tweet['author'] = quote['quoteAuthor']
            tweet['text'] = quote['quoteText']
            tweet['created_at'] = datetime.datetime.now().isoformat()

            r = requests.post(url,json=tweet)
            time.sleep(0.5)


if __name__ == "__main__":
    main()
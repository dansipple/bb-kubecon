#!/usr/bin/python

import time
import requests
import json
import datetime

# Infinite loop; we can use `kubectl scale` to turn this on and off

url = 'http://35.195.162.45/stream/add-quotes/'
# url = 'http://localhost:8080/add-quotes/'
quote = { 'author': 'Albert Einstein', 'text': 'Imagine is more important than knowledge.'}

# https://github.com/4skinSkywalker/Database-Quotes-JSON

def main():

    quote['created_at'] = datetime.datetime.now().isoformat()

    while True:
        print('sending payload', json.dumps(quote,indent=2))
        r = requests.post(url,json=quote)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
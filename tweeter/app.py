#!/usr/bin/python

import time
import requests
import json

# Infinite loop; we can use `kubectl scale` to turn this on and off

url = 'http://35.195.162.45/stream/add-quotes/'
# url = 'http://localhost:8080/add-quotes/'
quote = { 'author': 'Albert Einstein', 'created_at': '2012-04-05', 'text': 'Imagine is more important than knowledge.'}

# https://github.com/4skinSkywalker/Database-Quotes-JSON

def main():
    while True:
        print('sending payload')
        r = requests.post(url,json=quote)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
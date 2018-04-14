#!/usr/bin/python

import time
import requests

# Infinite loop; we can use `kubectl scale` to turn this on and off

url = 'http://35.195.162.45'
url = 'http://localhost:8080/add-quotes/'
payload = { 'tweet': 'Hello, world.'}

# https://github.com/4skinSkywalker/Database-Quotes-JSON

def main():
    while True:
        print('sending payload')
        r = requests.post(url,payload)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
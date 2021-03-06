#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get('https://swapi.co/api/people' +
                       '/?search={}'.format(sys.argv[1]))
    print('Number of results: {}'.format(req.json().get('count')))
    for names in req.json().get('results'):
        print(names.get('name'))

#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print('{}'.format(req.json().get('id')))

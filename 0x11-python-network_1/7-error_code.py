#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""

import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code < 400:
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))

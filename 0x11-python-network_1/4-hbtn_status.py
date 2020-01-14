#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""

import urllib.request
import urllib.parse
import sys
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))

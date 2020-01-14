#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        a_dict = {'q': ''}
    elif len(sys.argv) > 1:
        a_dict = {'q': sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', a_dict)
    if 'json' not in req.headers.get('content-type'):
        print('Not a valid JSON')
    else:
        if req.json():
            print('[{}] {}'.format(req.json().get('id'),
                                   req.json().get('name')))
        else:
            print('No result')

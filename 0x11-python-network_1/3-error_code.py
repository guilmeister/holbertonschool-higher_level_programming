#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except urllib.error.HTTPError as error_code:
        error_list = str(error_code).split()
        print('Error code: {}'.format(error_list[2][:-1]))

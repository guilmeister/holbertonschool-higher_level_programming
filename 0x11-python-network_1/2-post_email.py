#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as response:
        html = response.read()
        print(html.decode('UTF-8'))

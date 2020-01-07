#!/bin/bash
#Script that takes in a URL and displays all HTTP method server will accept
curl --silent --head "$1" | grep Allow | cut --complement -d' ' -f1

#!/bin/bash
#Script that takes in a URL as an argument, sends a GET request to the URL
curl --silent GET --header "X-HolbertonSchool-User-Id: 98" "$1"

#!/bin/bash
#Script that takes in a URL, request and displays size of body response
curl --silent "$1" | wc -c
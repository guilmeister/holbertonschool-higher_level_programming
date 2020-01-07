#!/bin/bash
#Script that takes in a URL and displays all HTTP method server will accept
curl -sI "$1" | grep Allow | cut -d' ' -f2-4

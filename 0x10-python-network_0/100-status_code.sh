#!/bin/bash
#Script that sends a request to a URL passed as an argument
curl --silent --output /dev/null --head --write-out "%{http_code}" "$1"

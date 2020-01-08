#!/bin/bash
#Script that sends a JSON POST request to a URL passed as the first argument
curl --silent POST --header "Content-Type: application/json" --data @"$2" "$1"

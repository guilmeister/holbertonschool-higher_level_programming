#!/bin/bash
#Script that takes in a URL as an argument, sends a GET request to the URL
curl --silent POST --data "email=hr@holbertonschool.com" --data "subject=I will always be here for PLD" "$1"

#!/bin/bash
#Script that sends a request to a URL passed as an argument
curl --silent --location GET "$1"

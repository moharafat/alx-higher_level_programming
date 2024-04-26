#!/bin/bash
#takes in a URL, sends a request to that URL
# thendisplays the size of the response body
curl -s "$1" | wc -c
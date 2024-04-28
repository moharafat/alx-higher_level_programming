#!/usr/bin/python3
""" script takesa URL, sends a request to the URL displays
 the value of the variable X-Request-Id in the response header"""
import sys
import requests
if __name__ == "__main__":
    URL = sys.argv[1]
    response = requests.get(URL)
    print(response.headers.get('X-Request-Id'))

#!/usr/bin/python3
"""takes URL, Dispalys X-Request-Id value"""
import sys
import urllib
import urllib.request
if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        print(response.headers.get('X-Request-Id'))

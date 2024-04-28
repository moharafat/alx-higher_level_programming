#!/usr/bin/python3
"""takes URL, Dispalys X-Request-Id value"""
import sys
import urllib
import urllib.request
if __name__ == "__main__":
    URL = sys.argv[1]
    REQUEST = urllib.request(URL) as response:
    with urllib.request.urlopen(REQUEST) as response:
        print(response.headers.get('X-Request-Id'))

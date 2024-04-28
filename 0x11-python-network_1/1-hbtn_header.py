#!/usr/bin/python3
""" Script tales URL, sends a request to the URL
"""
import sys
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
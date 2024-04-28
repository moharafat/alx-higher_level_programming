#!/usr/bin/python3
""" takes in a URL and an email, sends POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib
import urllib.parse
import urllib.request
if __name__ == "__main__":
    URL = sys.argv[1]
    VALUES = {"email": sys.argv[2]}
    DATA = urllib.parse.urlencode(VALUES).encode("ascii")

    req = urllib.request.Request(URL, DATA)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))

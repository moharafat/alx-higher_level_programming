#!/usr/bin/python3
"""  takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import sys
import urllib
import urllib.parse
import urllib.request
if __name__ == "__main__":
    URL = sys.argv[1]
    REQ = urllib.request.Request(URL)
    try:
        with urllib.request.urlopen(REQ) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as ERRORR:
        print("Error code: {}".format(ERRORR))

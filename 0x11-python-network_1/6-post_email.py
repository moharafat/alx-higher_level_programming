#!/usr/bin/python3
""" takes in a URL and an email, sends POST request to the passed URL with the
email as a parameter, and finally displays the body of the response
"""
import sys
import requests
if __name__ == "__main__":
    URL = sys.argv[1]
    VALUES = {"email": sys.argv[2]}
    response = requests.post(URL, VALUES)

    print(response.text)

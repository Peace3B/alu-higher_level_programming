#!/usr/bin/python3
"""
Fetches http://0.0.0.0:5050/status and displays the body response in a specific format.
"""
import urllib.request

if __name__ == "__main__":
    url = 'http://0.0.0.0:5050/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body).__name__))
        print("\t- content: {}".format(body.decode('utf-8')))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))

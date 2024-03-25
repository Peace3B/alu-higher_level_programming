#!/usr/bin/python3
"""
This module contains a script that takes in a URL, sends a request to the URL,
and displays the value of the `X-Request-Id` variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = urllib.request.Request(url)
        
        with urllib.request.urlopen(req) as response:
            # Retrieve the headers and convert them to a dictionary
            headers = dict(response.info())

            # Print the `X-Request-Id` from the headers if present
            print(headers.get("X-Request-Id"))

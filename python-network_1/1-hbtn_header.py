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
            # Retrieve the X-Request-Id header
            x_request_id = response.getheader('X-Request-Id')

            # If the X-Request-Id header is present, print its value
            if x_request_id:
                print(x_request_id)
            else:
                print("No X-Request-Id header found.")

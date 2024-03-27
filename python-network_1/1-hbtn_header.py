#!/usr/bin/python3
<<<<<<< HEAD
"""A script that displays the value of the x-request ID."""


if __name__ == '__main__':
    from urllib.request import urlopen
    import sys

    with urlopen(sys.argv[1]) as re:
        header_var = re.headers.get('X-Request-Id')
        print(header_var)
=======
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
>>>>>>> 23d5e9bba096ec7a90eef953679f03267ea1454c

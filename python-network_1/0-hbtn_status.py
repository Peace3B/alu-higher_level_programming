<<<<<<< HEAD
#!usr/bin/python3
import urllib.request

url = "https://intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
except Exception as e:
    print("Error fetching URL:", e)
=======
#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status."""
import urllib.request

if __name__ == "__main__":
    url = 'http://0.0.0.0:5050/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
>>>>>>> 23d5e9bba096ec7a90eef953679f03267ea1454c

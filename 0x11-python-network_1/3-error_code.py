#!/usr/bin/python3

"""Write a Python script that takes in a URL, sends a request to the URL"""

import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    req = sys.argv[1]
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

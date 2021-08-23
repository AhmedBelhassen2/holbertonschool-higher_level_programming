#!/usr/bin/python3

"""Write a Python script that takes in a URL, sends a request to the URL"""

import requests
import sys

if __name__ == "__main__":
    URL = requests.get(sys.argv[1])
    print(URL.headers.get('x-request-id'))

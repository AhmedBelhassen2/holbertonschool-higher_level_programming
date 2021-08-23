#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
"""
import urllib.request
import sys

if __name__ == "__main__":
    URL = sys.argv[1]
    with urllib.request.urlopen(URL) as response:
        print(response.getheader('X-Request-Id'))

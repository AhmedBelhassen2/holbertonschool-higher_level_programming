#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as resp:
        print(resp.read().decode('utf-8'))

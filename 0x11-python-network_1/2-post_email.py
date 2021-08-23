#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request
"""
import urllib.request
import sys


if __name__ == "__main__":
    param = urllib.parse.urlencode({'email': sys.argv[2]})
    param = param.encode('ascii')
    with urllib.request.urlopen(sys.argv[1], param) as resp:
        print(resp.read().decode('utf-8'))

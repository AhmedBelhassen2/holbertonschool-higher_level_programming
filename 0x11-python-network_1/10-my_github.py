#!/usr/bin/python3
""" Write a Python script that takes your GitHub credentials """
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    login = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=login)
    print(req.json().get("id"))

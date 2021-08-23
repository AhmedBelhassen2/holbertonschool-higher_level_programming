#!/usr/bin/python3

"""Take URL"""

import requests
import sys

if __name__ == "__main__":
    data = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(data.text)

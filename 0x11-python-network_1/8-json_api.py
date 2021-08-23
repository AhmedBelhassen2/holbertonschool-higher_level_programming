#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
"""
import requests
import sys

if __name__ == "__main__":

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': q}).json()
        if 'id' in response and 'name' in response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

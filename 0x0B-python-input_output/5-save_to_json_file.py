#!/usr/bin/python3
"""
JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ returns the JSON representation of an object (string) """
    with open(filename, "w") as f:
        return json.dump(my_obj, f)

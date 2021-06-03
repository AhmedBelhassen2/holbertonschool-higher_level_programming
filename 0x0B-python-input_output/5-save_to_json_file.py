#!/usr/bin/python3
"""
JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """ returns the JSON representation of an object (string) """
    return json.dumps(my_obj)

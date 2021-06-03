#!/usr/bin/python3
"""
JSON add
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file')

args = sys.argv[1:]
with open("add_item.json", "a")
    try:
        list = load_from_json_file("add_item.json")
    except Exception:
        list = []
    list += args
    save_to_json_file(list, "add_item.json")

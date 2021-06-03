#!/usr/bin/python3
"""
JSON add
"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
with open('add_item.json', 'a') as f:
    try:
        l = load_from_json_file('add_item.json')
    except:
        l = []
    l += args
    save_to_json_file(l, 'add_item.json')

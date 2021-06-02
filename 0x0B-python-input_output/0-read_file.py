#!/usr/bin/python3
"""
"""


def read_file(filename=""):
    """ read file """
    with open(filename, encoding="utf-8") as f:
        for l in f:
            print(l, end="")

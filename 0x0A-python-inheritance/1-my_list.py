#!/usr/bin/python3
"""
simple module
"""


class MyList(list):
    def print_sorted(self):
        """ function to sort list """
        print(sorted(self))
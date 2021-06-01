#!/usr/bin/python3

"""
inherit function
"""


def inherits_from(obj, a_class):
    """ inherit fn """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    else:
        return False

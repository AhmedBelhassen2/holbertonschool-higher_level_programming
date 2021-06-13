#!/usr/bin/python3
"""
Module text_indentation

"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    a = 0
    while a < len(text):
        if text[a] in [':', '.', '?']:
            print(text[a])
            print()
            a += 1
        else:
            print(text[a], end='')
        a += 1

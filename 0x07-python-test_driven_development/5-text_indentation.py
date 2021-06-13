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

    for char in text:
        st += char

        if char in special:
            print(st.strip())
            print()
            st = ''

    print(st.strip(), end='')

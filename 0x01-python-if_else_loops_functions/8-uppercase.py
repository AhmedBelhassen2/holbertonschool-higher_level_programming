#!/usr/bin/python3
def uppercase(str):
    for A in str:
        if 123 > ord(A) > 96:
            A = chr(ord(A) - 32)
        print("{}".format(A), end="")
    print('')

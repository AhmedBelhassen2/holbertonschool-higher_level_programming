#!/usr/bin/python
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        sum = add(a, b)
        for s in range(4, 6):
            sum = add(sum, s)
        return sum
    else:
        return sub(a, b)

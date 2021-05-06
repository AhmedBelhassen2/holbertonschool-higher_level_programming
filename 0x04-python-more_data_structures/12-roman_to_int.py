#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return(0)
    rm_vl = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_vl = 0
    for i in range(len(roman_string)):
        if i > 0 and rm_vl[roman_string[i]] > rm_vl[roman_string[i - 1]]:
            int_vl += rm_vl[roman_string[i]] - 2 * rm_vl[roman_string[i - 1]]
        else:
            int_vl += rm_vl[roman_string[i]]
    return int_vl

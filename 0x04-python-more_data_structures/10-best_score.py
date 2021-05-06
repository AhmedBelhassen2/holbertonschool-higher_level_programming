#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for k in a_dictionary:
        if a_dictionary[k] == max(a_dictionary.values()):
            return k

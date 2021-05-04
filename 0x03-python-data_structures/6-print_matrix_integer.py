#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lgn in matrix:
        for cln in lgn:
            print("{:d}".format(cln), end=" " if cln != lgn[-1] else"")
        print()

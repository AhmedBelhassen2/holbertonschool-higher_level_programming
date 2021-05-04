#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for columns in rows:
            if columns != rows[-1]:
                print("{:d}".format(cl), end=" ")
            else:
                print("{:d}".format(cl), end=" ")
        print("")

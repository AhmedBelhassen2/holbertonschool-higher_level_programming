#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
for rows in matrix: 
    for columns in rows: 
        print("{:d}".format(matrix[rows][columns]), end=' ' if not (columns == len(matrix[rows]) - 1):)        
        print() 

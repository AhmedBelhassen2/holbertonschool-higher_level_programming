#!/usr/bin/python3

"""
This module contains one function:
matrix_divided(matrix, div) -> returns a new matrix
"""

def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/float")
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if i != len(matrix) -1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same size")
        for elem in matrix[i]:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(""matrix must be a matrix (list of lists) of integers/floats"")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)
    return new_matrix

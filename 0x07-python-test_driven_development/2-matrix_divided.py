#!/usr/bin/python3
'''
The 2-matrix_divided module
This module has a function that divides a matrix
'''


def matrix_divided(matrix, div):
    '''
    The function that divides all elements of a matrix
    '''
    count = 0
    err_must_be = 'matrix must be a matrix (list of lists) of integers/floats'
    err_row_count = 'Each row of the matrix must have the same size'
    err_div = 'div must be a number'
    err_div_zero = 'division by zero'

    if isinstance(matrix, list) is False:
        raise TypeError(err_must_be)

    if len(matrix) is 0 or matrix == [[]]:
        raise TypeError(err_must_be)

    for ele in matrix:
        if isinstance(ele, list) is False:
            raise TypeError(err_must_be)
        for num in ele:
            if type(num) is not int and type(num) is not float:
                raise TypeError(err_must_be)

    if len(matrix) > 1:
        count = len(matrix[1])
        for ele in matrix:
            if count is not len(ele):
                raise TypeError(err_row_count)

    if type(div) is not int and type(div) is not float:
        raise TypeError(err_div)

    if div is 0:
        raise ZeroDivisionError(err_div_zero)

    return [[round(num / div, 2) for num in ele] for ele in matrix]

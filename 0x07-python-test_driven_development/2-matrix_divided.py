#!/usr/bin/python3
"""
Module Devide Matrix
    """


def matrix_divided(matrix, div):
    """
        Devides all elements in matrix
        Args:
            matrix (list[list[int/float]]) : matrice
            div (int/float) Devider
        Raise:
            TypeError: div not int or float
            TypeError: matix is not a list of list of number
            ZeroDivisionError: Div is 0
        Return : New matrix Devided
        """
    count = 0
    Error1 = 'matrix must be a matrix (list of lists) of integers/floats'
    Error2 = 'Each row of the matrix must have the same size'

    if isinstance(matrix, list) is False:
        raise TypeError(Error1)

    if len(matrix) is 0 or matrix == [[]]:
        raise TypeError(Error1)
    for elm in matrix:
        if isinstance(elm, list) is False:
            raise TypeError(Error1)
        for n in elm:
            if type(n) is not int and type(n) is not float:
                raise TypeError(Error1)

    if len(matrix) > 1:
        count = len(matrix[1])
        for elm in matrix:
            if count is not len(elm):
                raise TypeError(Error2)
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    if div is 0:
        raise ZeroDivisionError('division by zero')
    return [[round(n / div, 2) for n in elm] for elm in matrix]

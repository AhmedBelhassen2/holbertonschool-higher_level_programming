#!/usr/bin/python3
""" Module Square """
class Square:
    """ class Square that defines a square:
    size must be an integer
    size must not be negative """
    def __init__(self, size=0):
        """ initializes the square,  sets size equal to 0 by default,
        checks if size has the correct type and value """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

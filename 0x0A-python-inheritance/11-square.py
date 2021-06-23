#!/usr/bin/python3
""" class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class.
    """
    def __init__(self, size):
        """
        init fn
        """
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area fn
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        str fn
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)

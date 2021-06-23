#!/usr/bin/python3
"""
inheritance fn
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the rectangle class """
    def __init__(self, width, height):
        """ init fn """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__height = height
        self.__width = width

    def area(self):
        """
        the area() method must be implemented
        """
        return self.__height * self.__width

    def __str__(self):
        """
        str fn
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

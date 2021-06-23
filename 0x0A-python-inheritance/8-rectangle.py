#!/usr/bin/python3
""" inheritance fn """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the rectangle class """
    def __init__(self, width, height):
        """ init fn """
        self.__width = width
        self.integer_validator("width", width)
        self.height = height
        self.integer_validator("height", height)
        
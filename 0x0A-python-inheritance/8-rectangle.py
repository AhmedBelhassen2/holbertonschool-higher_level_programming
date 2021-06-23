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

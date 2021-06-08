#!/usr/bin/python3
"""
simple Rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @property
    def height(self):
        """ height Getter """
        return self.__height

    @property
    def x(self):
        """ x Getter """
        return self.__x

    @property
    def y(self):
        """ y Getter """
        return self.__y

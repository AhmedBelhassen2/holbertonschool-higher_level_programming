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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    @width.setter
    def width(self, value):
        """ Width Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height Setter """
        if type(value) is not int:
                raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Width Setter """
        if type(value) is not int:
                raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ that returns the area value of the Rectangle instance. """
        return self.__width * self.__height

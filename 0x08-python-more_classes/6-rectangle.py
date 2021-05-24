#!/usr/bin/python3
"""
module contains one class
"""


class Rectangle:
    """ class Rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instantiation """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        ch = ""
        if self.__width == 0 or self.__height == 0:
            return ch
        for j in range(self.__height):
            for i in range(self.__width):
                ch += "#"
            if j < self.__height - 1:
                ch += '\n'
        return ch

    def __repr__(self):
        """ return a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ called when an object is deleted with del """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

#!/usr/bin/python3
"""
module contains one class
"""


class Rectangle:
    """ class Rectangle """
    number_of_instances = 0

    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance that is a square w/ h==w==size"""
        return cls(size, size)

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
                ch += str(self.print_symbol)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

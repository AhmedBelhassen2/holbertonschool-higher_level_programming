#!/usr/bin/python3
"""
base class
"""


class BaseGeometry:
    """ the class """

    def area(self):
        """ area fn """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validater fn """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

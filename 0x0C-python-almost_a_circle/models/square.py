#!/usr/bin/python3
""" simple class square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Size Getter """
        return self.width

    @size.setter
    def size(self, value):
        """ Size Setter """
        self.height = value
        self.width = value

    def __str__(self):
        """ informal string representation of the square """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

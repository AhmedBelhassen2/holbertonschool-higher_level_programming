#!/usr/bin/python3
""" simple class square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''get the size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set value to the size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """ informal string representation of the square """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """ update """
        j = 0
        if args:
            for arg in args:
                if j == 0:
                    self.id = arg
                if j == 1:
                    self.size = arg
                if j == 2:
                    self.x = arg
                if j == 3:
                    self.y = arg
                j += 1
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        ''' the dictionary representation of a Square '''
        dict_ = {}
        dict_.update({"id": self.id,
                      "x": self.x,
                      "size": self.size,
                      "y": self.y
                      })
        return dict_

#!/usr/bin/python3
"""
simple Rectangle.
"""
from rec.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

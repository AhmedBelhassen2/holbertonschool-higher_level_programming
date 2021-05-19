#!/usr/bin/python3
""" Module Square """


class Square:
    """ class Square that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ initializes the object """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ gets the value of __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of __size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((type(value) is not tuple) or (len(value) != 2)) \
            or (type(value[0]) is not int) \
            or (type(value[1]) is not int) \
                or ((value[0] < 0) or (value[1] < 0)):
            else TypeError("position must be a tuple of 2 positive integers")

        def area(self):
            return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for l in range(self.position[1]):
                    print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

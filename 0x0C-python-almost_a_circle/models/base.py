#!/usr/bin/python3
""" base class """


class Base:
    """ This class will be the “base” of all other classes in this project """

    __nb_objects = 0

    def __init__(self, id=None):
        """  the public instance attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSONis one of the standard formats for sharing data representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

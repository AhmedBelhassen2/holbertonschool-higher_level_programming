#!/usr/bin/python3
""" base class """

import json


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
        """ JSON is representation """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ returns the JSON representation of an object (string) """
        l = []
        if list_objs is None or list_objs == []:
            list_objs = []
        for j in list_objs:
            l.append(cls.to_dictionary(j))
        with open('{}.json'.format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        """ json_string is a string representing a list of dictionaries """
        if json_string is None:
            return []
        return json.loads(json_string)

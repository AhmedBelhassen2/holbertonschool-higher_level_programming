#!/usr/bin/python3
""" simple module """


class Student:
    '''Student class
    '''

    def __init__(self, first_name, last_name, age):
        '''defines a student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            d = {}
            for names in attrs:
                if hasattr(self, names):
                    d[names] = getattr(self, names)
            return (d)

#!/usr/bin/python3
"""
12-student

"""


class Student:
    """
Write a class Student that defines a student by atribs
    """
    def __init__(self, first_name, last_name, age):
        """
     first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public class method json
        """
        if attrs is None:
            return (self.__dict__)
        else:
            keys = {}
            for item in attrs:
                if hasattr(self, item):
                    keys[item] = getattr(self, item)
            return (keys)

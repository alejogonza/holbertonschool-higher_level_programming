#!/usr/bin/python3
"""
13-student

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

    def reload_from_json(self, json):
        """public class method
        Replaces all attributes of the Student instance
        """
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]

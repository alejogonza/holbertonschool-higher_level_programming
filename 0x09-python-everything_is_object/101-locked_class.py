#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

    def __init__(self, name=""):

        if type(name) is str:
            self.first_name = name

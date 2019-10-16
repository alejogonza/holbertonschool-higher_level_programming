#!/usr/bin/python3
"""
 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    checks instance of a specified class

    """
    return isinstance(obj, a_class) and obj.__class__ != a_class

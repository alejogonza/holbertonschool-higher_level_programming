#!/usr/bin/python3
def add_attribute(ob, nm, val):
    """
    Function that adds a new attribute to an object
    """

    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, nm, val)

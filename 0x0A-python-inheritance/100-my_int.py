#!/usr/bin/python3
class MyInt(int):
    """ inhers from int"""

    def __eq__(self, new):
        return int.__ne__(self, new)

    def __ne__(self, new):
        return int.__eq__(self, new)

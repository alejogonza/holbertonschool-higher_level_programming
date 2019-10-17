#!/usr/bin/python3
"""
 4-append_write

"""


def append_write(filename="", text=""):
    """
function that appends a string at the
end of a text file and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        charcount = my_file.write(text)
    return (charcount)

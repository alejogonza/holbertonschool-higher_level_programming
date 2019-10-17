#!/usr/bin/python3
"""docstring"""


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found
    Args:
        filename: filename
        search_string: string to search
        new_string: string to append
    """

    rline = []

    with open(filename, 'r', encoding="utf-8") as f:
        for linep in f:
            rline += [linep]
            if linep.find(search_string) != -1:
                rline += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(rline))

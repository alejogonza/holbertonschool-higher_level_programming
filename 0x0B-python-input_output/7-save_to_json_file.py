#!/usr/bin/python3
import json
"""
 7-save_to_json_file

"""


def save_to_json_file(my_obj, filename):
    """
    function that writes Object to text file,
    using a JSON representation:

    """
    with open(filename, 'w') as my_file:
        my_file.write(json.dumps(my_obj))

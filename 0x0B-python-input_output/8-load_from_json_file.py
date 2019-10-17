#!/usr/bin/python3
import json
"""
 8-load_from_json_file

"""


def load_from_json_file(filename):
    """
    Write a function that creates an Object from a "JSON file"
    """
    with open(filename, encoding='utf-8') as my_file:
        return json.load(my_file)

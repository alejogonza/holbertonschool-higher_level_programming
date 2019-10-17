#!/usr/bin/python3
"""
9-add_item

"""

import sys


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def load_add_save(filename, args):
    """
    script that adds all args to a Python list, and sabe un

    """
    try:
        newjson = load_from_json_file(filename)
    except FileNotFoundError:

        newjson = []
        newjson = save_to_json_file(newjson + args, filename)

    if __name__ == "__main__":
        filename = "add_item.json"
        load_add_save(filename, sys.argv[1:])

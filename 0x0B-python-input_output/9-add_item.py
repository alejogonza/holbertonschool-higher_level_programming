#!/usr/bin/python3
"""
9-add_item
"""
import sys
import os.path


save_json_file = __import__('7-save_to_json_file').save_to_json_file

load_json_file = __import__('8-load_from_json_file').load_from_json_file

formater = []

if os.path.exists("add_item.json"):
    formater = load_json_file("add_item.json")

for arg in sys.argv[1:]:
    formater.append(arg)

save_json_file(formater, "add_item.json")

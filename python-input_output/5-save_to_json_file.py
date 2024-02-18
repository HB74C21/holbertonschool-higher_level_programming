#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.
    """
    with open(filename, "w") as fd:
        json.dump(my_obj, fd)

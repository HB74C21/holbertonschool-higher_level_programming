#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”:
"""


import json


def load_from_json_file(filename):
    """
    Load a JSON file into a Python object.
    """
    with open(filename, "r") as fd:
        data = json.load(fd)

        return data

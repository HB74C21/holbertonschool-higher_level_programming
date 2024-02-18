#!/usr/bin/python3
"""
function that returns the JSON representation of an object (string)
"""


import json

def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.
    """
    data_json__string = json.dumps(my_obj)

    return data_json__string

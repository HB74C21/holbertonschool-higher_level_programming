#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string:
"""


import json


def from_json_string(my_str):
    """
    Returns Python object represented by my_str,
    which is a valid JSON string.
    """

    data_json_string = json.loads(my_str)

    return data_json_string

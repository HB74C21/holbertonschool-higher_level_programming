#!/usr/bin/python3
"""
This file defines a Base class.
"""

import json


class Base:
    """
    Base class for creating objects with a unique identifier.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.
        """
        self.id = id

        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id

    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string
        """
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

#!/usr/bin/python3
"""
This module defines a function that writes a given text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a given text to a file.
    """
    with open(filename, "w", encoding="utf-8") as fd:
        new_file = fd.write(text)
    return new_file

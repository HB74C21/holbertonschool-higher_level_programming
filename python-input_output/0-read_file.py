#!/usr/bin/python3
"""
Read the contents of a file and print them to the console.
"""


def read_file(filename=""):
    """
    A function to read the contents of a file.
    """
    with open(filename, encoding="utf-8") as fd:
        read_data = fd.read()

        print(read_data)

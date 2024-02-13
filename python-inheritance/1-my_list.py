#!/usr/bin/python3
"""
This script defines a MyList class that inherits from the built-in list class.
"""


class MyList(list):
    """
    The MyList class inherits from the list class
    and adds a print_sorted method to print the sorted list.
    """

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

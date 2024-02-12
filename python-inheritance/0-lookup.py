#!/usr/bin/python3
"""
Function that returns the list of available attribute and methods of an object
"""


def lookup(obj):
    liste = dir(obj)
    return liste

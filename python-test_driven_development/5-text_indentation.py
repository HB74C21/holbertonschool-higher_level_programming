#!/usr/bin/python3
"""
This module defines a function to print
a text with 2 new lines after each
occurrence of '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    for char in text:
        print(char, end="")
        if char in punctuation:
            print("\n")
    print()

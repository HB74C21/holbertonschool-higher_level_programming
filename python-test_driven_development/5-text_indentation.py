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

    punctuation = [".", "?", ":"]
    new_line = True
    for char in text:
        if new_line and char == ' ':
            continue
        elif char == "\n":
            new_line = True
        elif char in punctuation:
            print(char + "\n\n", end="")
            new_line = True
        else:
            print(f"{char}", end="")
            new_line = False

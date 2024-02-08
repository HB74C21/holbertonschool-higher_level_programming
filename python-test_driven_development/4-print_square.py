#!/usr/bin/python3
"""
    Ce script définit une fonction pour imprimer un carré avec le caractère #
"""


def print_square(size):
    """
        Imprime un carré avec le caractère
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

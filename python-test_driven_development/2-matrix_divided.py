#!/usr/bin/python3
"""
function that divides
all elements
of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor
    """
    if not isinstance(matrix, list) \
        or not all(isinstance(row, list)
                   and all(isinstance(element, (int, float))
                           for element in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

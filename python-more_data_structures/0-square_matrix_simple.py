#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[0])):
            new_row.append(matrix[i][j] * matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix

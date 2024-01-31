#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colum in row:
            print("{:d}".format(colum), end=" ")
        print()

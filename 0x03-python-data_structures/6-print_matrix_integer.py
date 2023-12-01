#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    """prints the matrix of integers"""

    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()

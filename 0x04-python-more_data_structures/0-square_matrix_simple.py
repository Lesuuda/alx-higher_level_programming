#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    """
    computes the square values of all integers of a matrix
    takes a matrix as parameter
    return the new matrix, with same size and square value
    """

    result_matrix = []
    for row in matrix:
        result_row = []
        for element in row:
            result_row.append(element ** 2)
        result_matrix.append(result_row)
    return result_matrix

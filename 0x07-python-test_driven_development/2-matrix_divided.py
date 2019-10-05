#!/usr/bin/python3
"""Module to find the matrix divided by div



"""


def matrix_divided(matrix, div):
    """Function to find the matrix divided by div

    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    for outer in range(0, len(matrix)):
        for inner in range(0, len(matrix[outer])):
            if inner > len(matrix):
                raise TypeError("Each row of the matrix must have the same\
 size")
            if isinstance(matrix[outer][inner], (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    field_reset = []
    new_matrix = []
    for outer in range(0, len(matrix)):
        field_reset = []
        for inner in range(0, len(matrix[outer])):
            quotient = round(matrix[outer][inner] / div, 2)
            field_reset.append(quotient)
        new_matrix.append(field_reset)
    return new_matrix

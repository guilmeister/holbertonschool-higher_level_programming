#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    field_reset = []
    new_matrix = []
    for outer in range(0, len(matrix)):
        field_reset = []
        for inner in range(0, len(matrix[outer])):
            squared = matrix[outer][inner] ** 2
            field_reset.append(squared)
        new_matrix.append(field_reset)
    return new_matrix

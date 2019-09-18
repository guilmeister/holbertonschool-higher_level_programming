#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for index_value in x:
            if index_value != x[-1]:
                print("{:d}".format(index_value), end=" ")
            else:
                print("{:d}".format(index_value), end="")
            print("")

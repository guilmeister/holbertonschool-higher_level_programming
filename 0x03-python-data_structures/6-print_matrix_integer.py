#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for index_value in x:
            print("{:d}".format(index_value), end="")
            if index_value != x[-1]:
                print("", end=" ")
        print("")

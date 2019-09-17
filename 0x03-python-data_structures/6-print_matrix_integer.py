#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	if len(matrix) != 0:
		for x in range(len(matrix)):
			for y in range(len(matrix)):
				if y != len(matrix) - 1:
					print(matrix[x][y], end=" ")
				else:
					print(matrix[x][y], end="")
			print("")

#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    for x in range(0, n):
        triangle.append([])
        if x != 0:
            triangle[x].append(1)
        for y in range(1, x):
            triangle[x].append(triangle[x-1][y-1]+triangle[x-1][y])
        if n != 0:
            triangle[x].append(1)
#    a.insert(0, [1])
    return triangle

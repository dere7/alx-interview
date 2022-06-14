#!/usr/bin/python3
"""0-pascal_triangle.py"""


def pascal_triangle(n):
    """returns list of lists of integers
    representing the pascal triangle of n"""
    ls = []
    for i in range(0, n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(ls[i - 1][j - 1] + ls[i - 1][j])
        ls.append(row)
    return ls

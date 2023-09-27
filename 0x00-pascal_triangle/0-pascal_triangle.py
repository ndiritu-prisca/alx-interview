#!/usr/bin/python3
"""
    A function def pascal_triangle(n): that returns a list of lists of
    integers representing the Pascals triangle of n
    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
    """Function that returns list of lists of integers"""
    if n <= 0:
        return []

    triangle = []
    for x in range(n):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            for y in range(1, x):
                row.append(prev_row[y - 1] + prev_row[y])
            row.append(1)
        triangle.append(row)

    return triangle

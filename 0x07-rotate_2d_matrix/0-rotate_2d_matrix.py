#!/usr/bin/python3
"""Rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    """Function that rotates a 2d matrix"""
    n = len(matrix)

    # Transposing matrix
    for x in range(n):
        for y in range(x + 1, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    # Reversing each row to get the final result
    for i in range(n):
        matrix[i] = matrix[i][::-1]

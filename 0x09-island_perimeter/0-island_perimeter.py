#!/usr/bin/python3
"""Module to calculate perimeter of island"""


def island_perimeter(grid):
    """Function that returns the perimeter of the island described in grid"""
    if not grid or not grid[0]:
        return 0

    rows, columns = len(grid), len(grid[0])
    perimeter = 0

    for x in range(rows):
        for y in range(columns):
            if (grid[x][y] == 1):
                perimeter += 4

                if (y > 0 and grid[x][y - 1] == 1):
                    # Subtract 2 if left neighbor is land
                    perimeter -= 2

                if (x > 0 and grid[x - 1][y] == 1):
                    # Subtract 2 if top neighbor is land
                    perimeter -= 2

    return perimeter

#!/usr/bin/python3
"""Contains function that calculates perimeter of island"""


def island_perimeter(grid):
    """Contains function that calculates perimeter of island
       - grid : list of list of integer
            0 represents water and 1 represents land
    """
    perimeter = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter

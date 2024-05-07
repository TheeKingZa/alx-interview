#!/usr/bin/python3
"""
Module: 0-island_perimeter
Calculate the perimeter of the island described in the grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    - grid (list of list of int): A grid representing the island where:
        0 represents water
        1 represents land

    Returns:
    - int: The perimeter of the island

    Constraints:
    - The grid is completely surrounded by water
    - There is only one island (or nothing)
    - The island doesn’t have “lakes”
    (water inside that isn’t connected to the water surrounding
    the island)
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # For each land cell, add 4 to the perimeter
                perimeter += 4
                # Check if there is a land cell to the left
                if i > 0 and grid[i - 1][j] == 1:
                    # If there is, subtract 2 from the perimeter
                    perimeter -= 2
                # Check if there is a land cell above
                if j > 0 and grid[i][j - 1] == 1:
                    # If there is, subtract 2 from the perimeter
                    perimeter -= 2

    return perimeter  # Return the calculated perimeter

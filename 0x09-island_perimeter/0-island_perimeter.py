#!/usr/bin/python3
"""
Module: Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns:
      int: The perimeter of the island.
      returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for x1, x2 in zip([0] + row, row + [0]):
            area += int(x1 != x2)
    return area

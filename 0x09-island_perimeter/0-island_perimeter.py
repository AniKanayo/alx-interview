#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A rectangular grid representing the
        island, where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.

    Raises:
        None

    Examples:
        >>> grid = [[0, 1, 0, 0],
        ...         [1, 1, 1, 0],
        ...         [0, 1, 0, 0],
        ...         [1, 1, 0, 0]]
        >>> island_perimeter(grid)
        16
    """
    area = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            area += int(i1 != i2)
    return area

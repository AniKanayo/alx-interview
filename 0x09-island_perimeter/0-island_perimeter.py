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
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter

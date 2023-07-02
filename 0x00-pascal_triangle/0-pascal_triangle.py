#!/usr/bin/python3
"""
A modulen to return a list of lists of integers representing Pascal's triangle
"""


def pascal_triangle(n):
    """
    Pascal's triangle
    Args:
      n (int) represents the number of rows of the triangle
    Returns:
      a list of lists of integers representing the Pascal’s triangle
    """
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists

#!/usr/bin/python3
"""
A function to return a list of lists of integers representing Pascal's triangle
"""


def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Create a row with i+1 items & initialized to 1

        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

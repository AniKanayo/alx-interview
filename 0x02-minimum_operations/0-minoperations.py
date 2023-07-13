#!/usr/bin/python3
"""
Minimum operations: Python method that can be implemented within your own code
"""


def minOperations(n):
    """

    :param n: n: An integer representing the desired
    number of 'H' characters in the file.

    :return:An integer representing the fewest number of operations
    needed to result in exactly n 'H' characters in the file
    """
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op

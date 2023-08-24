#!/usr/bin/python3
"""
This function calculates the fewest number of coins
needed to meet a given total amount
"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to
    meet a given total amount

    Arguments:
    coins -- a list of coin values
    total -- the target total amount

    Returns:
    The fewest number of coins needed to meet the total
    amount, or -1 if it's not possible
    """
    if total <= 0:
        return 0

    dp = [0] + [float("inf")] * total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1

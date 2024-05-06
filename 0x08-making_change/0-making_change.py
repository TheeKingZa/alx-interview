#!/usr/bin/python3
'''
Coins of different values,
determine number of coins needed to meet
a given amount total.
'''
import sys


def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make a total amount.

    Args:
        coins (list of int): The denominations of available coins.
        total (int): The total amount to make change for.

    Returns:
        int: The minimum number of coins needed to make the total amount.
             Returns -1 if it's impossible to make the
             total amount with the given coins.
    """
    if total <= 0:
        return 0
    table = [sys.maxsize for i in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == sys.maxsize:
        return -1
    return table[total]

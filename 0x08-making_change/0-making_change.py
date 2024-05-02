#!/usr/bin/python3
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

    # If the total amount is non-positive, return 0 coins needed
    if total <= 0:
        return 0

    # Initialize a table to store minimum coins needed
    # for each amount from 0 to total
    table = [sys.maxsize for i in range(total + 1)]
    table[0] = 0  # Base case: 0 coins needed for 0 amount

    # Iterate over each amount from 1 to total
    for i in range(1, total + 1):
        # Iterate over each coin denomination
        for j in range(len(coins)):
            # If the coin value is less than or equal to the current amount
            if coins[j] <= i:
                # Calculate the minimum coins needed for the
                # remaining amount after using this coin
                subres = table[i - coins[j]]
                # Update the table if using this coin
                # leads to a smaller number of coins needed
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    # If it's impossible to make the total amount with
    # the given coins, return -1
    if table[total] == sys.maxsize:
        return -1

    # Otherwise, return the minimum number of coins needed for the total amount
    return table[total]

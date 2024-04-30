#!/usr/bin/python3


def makeChange(coins, total):
    """
    Calculates the minimum number of coins
    needed to make change for a given total.

    Args:
    coins (list): List of coin denominations available.
    total (int): Total amount for which change needs to be made.

    Returns:
    int: Minimum number of coins needed to make change for the total.
    Returns -1 if coins list is empty or None,
            or if total is less than or equal to 0.
    """
    # Check if coins list is empty or None
    if not coins or coins is None:
        return -1
    # Check if total is less than or equal to 0
    if total <= 0:
        return 0

    # Initialize the variable to store the total
    # number of coins needed for change
    change = 0

    # Sort the coins in descending order to
    # start with the largest denomination first
    coins = sorted(coins)[::-1]

    # Iterate through each coin denomination
    for coin in coins:
        # While the coin denomination is less than
        # or equal to the remaining total
        while coin <= total:
            # Subtract the coin denomination from the total
            total -= coin
            # Increment the count of coins used for change
            change += 1
        # If the total becomes 0, return the total count of coins used
        if total == 0:
            return change
    # If it's not possible to make exact change for the total, return -1
    return -1

#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list): List of coin denominations available.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet total.
        Returns -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over all possible amounts from 1 to total
    for i in range(1, total + 1):
        # Iterate over each coin denomination
        for coin in coins:
            # If the current coin value is less than or
            # equal to the current amount
            if coin <= i:
                # Update the fewest number of coins
                # needed for the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity,
    # total cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

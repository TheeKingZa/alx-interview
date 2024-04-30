#!/usr/bin/python3
import sys

def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to make change for a given total using dynamic programming.

    Args:
    coins (list): List of coin denominations available.
    total (int): Total amount for which change needs to be made.

    Returns:
    int: Minimum number of coins needed to make change for the total. Returns -1 if total is less than or equal to 0.
    """
    # Check if total is less than or equal to 0
    if total <= 0:
        return 0
    
    # Create a table to store minimum number of coins for each total amount from 0 to total
    # Initialize the table with a very large value
    table = [sys.maxsize for i in range(total + 1)]
    
    # Base case: 0 coins needed to make change for 0
    table[0] = 0
    
    m = len(coins)  # Number of coin denominations
    
    # Iterate over each amount from 1 to total
    for i in range(1, total + 1):
        # Iterate over each coin denomination
        for j in range(m):
            # If the current coin denomination is less than or equal to the current amount
            if coins[j] <= i:
                # Calculate the minimum number of coins needed for the remaining amount
                subres = table[i - coins[j]]
                # If the subresult is not the initial large value and it's smaller than the current table value
                if subres != sys.maxsize and subres + 1 < table[i]:
                    # Update the table with the minimum number of coins
                    table[i] = subres + 1
    
    # If it's not possible to make exact change for the total, return -1
    if table[total] == sys.maxsize:
        return -1
    # Otherwise, return the minimum number of coins needed for the total
    return table[total]

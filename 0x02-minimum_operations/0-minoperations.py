#!/usr/bin/python3
'''
Minimum Operations Python3 Challenge:
This script calculates the fewest number
of operations needed to result in exactly n H
characters in the file.
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations.
        If n is impossible to achieve, return 0.
    '''

    # Initialize variables
    pasted_chars = 1  # Represents the current number of characters in the file
    clipboard = 0     # Represents the number of H's copied to the clipboard
    counter = 0       # Counts the number of operations

    # Loop until the desired number of characters is achieved
    while pasted_chars < n:
        # If nothing is copied yet, perform a "Copy All" operation
        if clipboard == 0:
            clipboard = pasted_chars
            # Copy the current number of characters
            counter += 1
            # Increment the operation counter

        # If only one character is pasted, perform a "Paste" operation
        if pasted_chars == 1:
            pasted_chars += clipboard
            # Paste the characters from the clipboard
            counter += 1
            # Increment the operation counter
            continue
            # Continue to the next iteration

        # Calculate the remaining characters needed to reach the target
        remaining = n - pasted_chars

        # If the remaining characters are less
        # than the characters in the clipboard,
        # it's impossible to achieve the target number of characters
        if remaining < clipboard:
            return 0

        # If the remaining characters cannot
        # be evenly divided by the current characters,
        # paste the characters from the clipboard
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            # Paste the characters from the clipboard
            counter += 1
            # Increment the operation counter
        else:
            # If the remaining characters can
            # be evenly divided by the current characters,
            # perform a "Copy All" operation followed by a "Paste" operation
            clipboard = pasted_chars
            # Copy the current number of characters
            pasted_chars += clipboard
            # Paste the characters from the clipboard
            counter += 2
            # Increment the operation counter

    # Check if the desired number of characters is achieved
    if pasted_chars == n:
        return counter  # Return the total number of operations
    else:
        return 0        # Return 0 if the target is not achieved

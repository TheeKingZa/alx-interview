#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    # If n is less than or equal to 1, it's impossible to achieve, return 0
    if n <= 1:
        return 0

    operations = 0  # Initialize the number of operations needed
    i = 2  # Start from 2 as the smallest prime factor

    # Iterate from 2 to n
    while i <= n:
        # Check if i is a factor of n
        if n % i == 0:
            n //= i  # Divide n by i
            operations += i  # Add i to the total operations needed
        else:
            i += 1  # Move to the next number if i is not a factor

    return operations  # Return the total number of operations

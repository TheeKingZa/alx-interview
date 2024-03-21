#!/usr/bin/python3
def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
    - n: integer, the target number of H characters

    Returns:
    - integer, the minimum number of operations
    """

    if n <= 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        # Start with the assumption that the minimum operations for i is i.
        operations[i] = i
        for j in range(2, i):
            if i % j == 0:
                # If i is divisible by j, then we can perform j operations
                # to get i by copying j times and pasting.
                operations[i] = min(operations[i], operations[j] + i // j)
                # We also consider the case where we
                # paste i//j times after copying j characters.

    return operations[n]

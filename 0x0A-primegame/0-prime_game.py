#!/usr/bin/python3
"""
Prime Game Module

This module defines the function `isWinner` which determines
the winner of a prime
number game played by Maria and Ben over multiple rounds.
"""


def isWinner(x, nums):
    """
    Determines the winner of each game round and returns
    the name of the player
    who won the most rounds.
    If the number of rounds won by each player is equal,
    returns None.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int):
                    List of integers where each integer represents the maximum
                    number in the set for that round.

    Returns:
    str: "Maria" if Maria wins the most rounds,
        "Ben" if Ben wins the most rounds,
         or None if they win an equal number of rounds.
    """
    if x <= 0 or nums is None:
        return None
        # Edge case: no rounds or invalid input
    if x != len(nums):
        return None
        # Edge case: mismatch between number of rounds and length of nums

    ben = 0
    maria = 0

    # Create a list to mark prime numbers using the Sieve of Eratosthenes
    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0  # 0 and 1 are not primes

    # Apply the Sieve of Eratosthenes
    for i in range(2, len(a)):
        remove_mult(a, i)

    # Determine the winner for each round
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1  # Ben wins if the count of primes is even
        else:
            maria += 1  # Maria wins if the count of primes is odd

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None  # If both have the same number of wins


def remove_mult(ls, x):
    """
    Marks the multiples of x as non-prime (0) in the list ls.

    Parameters:
    ls (list of int): List where indices represent numbers and
    values indicate primality.
    x (int): The current prime number whose multiples are to be marked.

    Returns:
    None
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0  # Mark multiple as non-prime
        except (ValueError, IndexError):
            break  # Stop if the index goes out of range

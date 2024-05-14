#!/usr/bin/python3
"""
Prime Game Module

This module defines the function `isWinner` which
determines the winner of a prime
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
    nums (list of int): List of integers where each integer
                        represents the maximum
                        number in the set for that round.

    Returns:
    str: "Maria" if Maria wins the most rounds,
         "Ben" if Ben wins the most rounds,
         or None if they win an equal number of rounds.
    """
    def sieve(max_n):
        """
        Generates a list indicating prime numbers up to
        max_n using the Sieve of Eratosthenes.

        Parameters:
        max_n (int): The maximum number up to which
        primes need to be identified.

        Returns:
        list of bool: A list where index i is,
        True if i is a prime number, False otherwise.
        """
        # Initialize a list to mark primes,
        # assuming all numbers are prime initially
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        # 0 and 1 are not primes

        # Apply Sieve of Eratosthenes algorithm
        p = 2

        while (p * p <= max_n):
            if is_prime[p]:
                # Mark all multiples of p as non-prime
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime

    def game_winner(n, is_prime):
        """
        Simulates the game for a given n and determines the winner.

        Parameters:
        n (int): The maximum number in the set for this round.
        is_prime (list of bool): A list indicating prime
        numbers up to the maximum possible n.

        Returns:
        int: 0 if Maria wins, 1 if Ben wins.
        """
        # Generate a list of primes up to n
        primes = [i for i in range(1, n + 1) if is_prime[i]]
        turn = 0  # Maria starts the game (0 for Maria, 1 for Ben)

        # Simulate the game
        while primes:
            prime = primes[0]
            # Remove the chosen prime and
            # all its multiples from the list
            primes = [x for x in primes if x % prime != 0]
            turn = 1 - turn  # Switch turns

        return turn
        # The player who cannot make a move loses,
        # hence turn gives the winner

    # Edge case handling
    if x <= 0 or not nums:
        return None

    # Find the maximum value in nums to generate
    # primes up to that number
    max_n = max(nums)
    is_prime = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        winner = game_winner(n, is_prime)
        if winner == 1:  # Ben wins
            ben_wins += 1
        else:  # Maria wins
            maria_wins += 1

    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

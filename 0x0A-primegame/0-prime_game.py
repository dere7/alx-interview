#!/usr/bin/python3
"""solves prime game"""


def isPrime(x):
    """returns true if x is prime"""
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    determine the winner
        - x is number rounds
        - nums is an array of n
    """
    if x < 1:
        return
    ben = 0
    maria = 0
    for r in range(x):
        turn = 'M'
        n = list(range(1, nums[r] + 1))
        primes = list(filter(isPrime, n))
        for p in primes:
            n = list(filter(lambda x: x % p != 0, n))
            turn = 'B' if turn == 'M' else 'M'  # change turn

        if turn == 'M':
            ben += 1
        else:
            maria += 1

    return 'Maria' if maria > ben else 'Ben'


isWinner(3, [4, 5, 1])

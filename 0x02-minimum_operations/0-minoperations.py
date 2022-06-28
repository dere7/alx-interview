#!/usr/bin/python3
"""contains a functionthat calculates minimum
operations needed to result in n characters"""


def minOperations(n):
    """Given a number n, write a method that calculates the
    fewest number of operations needed to result in exactly
    n H characters in the file. only two operations in this file:
    Copy All and Paste allowed."""
    numH = 1
    operations = 0
    increment = 1
    while numH < n:
        if n % numH == 0:
            operations += 2  # copy All and paste
            increment = numH
        else:
            operations += 1  # paste
        numH += increment
    return operations

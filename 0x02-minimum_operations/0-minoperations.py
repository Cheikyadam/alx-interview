#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """the function here"""

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n = n // factor
        factor += 1

    return operations

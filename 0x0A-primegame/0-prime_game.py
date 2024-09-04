#!/usr/bin/python3
"""is Winner module"""


def isWinner(x, nums):
    """Function isWinner"""

    if x <= 0 or len(nums) == 0 or x > len(nums):
        return None

    maria = 0
    ben = 0
    for i in range(0, x):
        win = winner(i, nums[i])
        if win is True:
            maria += 1
        else:
            ben += 1
    if maria > ben:
        return "Maria"
    else:
        return "Ben"


def winner(i, n):
    """helper 1"""
    max = n
    prime_number = prime_n(max)
    if len(prime_number) == 0:
        return -1
    if len(prime_number) % 2 == 0:
        return False
    return True
    # for cur in
    # current_choice = best_choice(prime_number, max)
    # prime_number.remove(current_choice)


def best_choice(array_prime, max):
    """optimal choice"""
    if len(array_prime) == 0:
        return -1
    best_choice = array_prime[0]
    for prime in array_prime:
        choice = count_number_of_multiple(prime, max)
        if choice > best_choice:
            best_choice = choice
    return best_choice


def count_number_of_multiple(prime, max_value):
    """helper"""
    return max_value // prime


def prime_n(n):
    """helper 2"""
    tab = []
    for i in range(n+1):
        if is_prime(i):
            tab.append(i)
    return tab


def is_prime(number):
    """helper 3"""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """make change"""
    if total <= 0:
        return 0
    i = len(coins) - 1
    coins.sort()
    nb_coins = 0
    while i >= 0:
        curr = total // coins[i]
        nb_coins += curr
        total = total % coins[i]
        if total == 0:
            return nb_coins
        i -= 1
    if total != 0:
        return -1
    return nb_coins

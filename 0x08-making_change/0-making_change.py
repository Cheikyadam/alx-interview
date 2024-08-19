#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """make change"""
    if total <= 0:
        return 0
    i = len(coins) - 1
    nb_coins = 0
    while i >= 0:
        while total >= coins[i]:
            total -= coins[i]
            nb_coins += 1
        i -= 1
    if total != 0:
        return -1
    return nb_coins

#!/usr/bin/python3
"""Module for makeChange"""

def makeChange(coins, total):
    """Function that returns number of coins to make change"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    if total == 0:
        return num_coins
    else:
        return -1
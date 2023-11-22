#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    remainder = total

    for coin in coins:
        num_coins = remainder // coin
        coin_count += num_coins
        remainder %= coin

    if remainder != 0:
        return -1

    return coin_count

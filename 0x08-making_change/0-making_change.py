#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins_list = [float('inf')] * (total + 1)

    coins_list[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            coins_list[i] = min(coins_list[i], coins_list[i - coin] + 1)

    if coins_list[total] == float('inf'):
        return -1

    return coins_list[total]

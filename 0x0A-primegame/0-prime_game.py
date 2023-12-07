#!/usr/bin/python3
"""
Prime number game solution
"""


def list_prime_nums(n):
    """Return list of prime numbers between 1 and n inclusive
    """
    prime_nums = []
    sieve = [True] * (n + 1)
    for x in range(2, n + 1):
        if (sieve[x]):
            prime_nums.append(x)
            for i in range(x, n + 1, x):
                sieve[i] = False
    return prime_nums


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria_wins = Ben_wins = 0
    for i in range(x):
        prime_nums = list_prime_nums(nums[i])
        if len(prime_nums) % 2 == 0:
            Ben_wins += 1
        else:
            Maria_wins += 1
    if Maria_wins > Ben_wins:
        return 'Maria'
    elif Ben_wins > Maria_wins:
        return 'Ben'
    return None

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def play_round(n):
    """Simulate a round of the game."""
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    moves = set()

    while primes:
        max_prime = max(primes)
        moves.add(max_prime)
        primes = [num for num in primes if num % max_prime != 0]

    return moves

def isWinner(x, nums):
    """Determine the winner of each round."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = play_round(n)

        if x % 2 == 1:
            # Maria's turn
            if moves:
                maria_wins += 1
        else:
            # Ben's turn
            if not moves:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

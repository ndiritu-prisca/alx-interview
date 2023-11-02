#!/usr/bin/python3
"""Challenge of placing N non-attacking queens on an N×N chessboard"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

num = int(sys.argv[1])


def nQueens(num, x=0, a=[], b=[], c=[]):
    """Solves the N queens problem."""
    if x < num:
        for j in range(num):
            if j not in a and x + j not in b and x - j not in c:
                yield from nQueens(num, x + 1, a + [j], b + [x + j], c + [x - j])
    else:
        yield a


def solution(num):
    """Method to solve """
    x = 0
    k = []
    for ans in nQueens(num, 0):
        for a in ans:
            k.append([x, a])
            x += 1
        print(k)
        k = []
        x = 0


solution(num)

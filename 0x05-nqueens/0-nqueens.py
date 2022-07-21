#!/usr/bin/python3
"""program that solves N Queens Problem"""
import sys


def construct_candidate(a, N: int):
    """gets candidates for a configuration"""
    candidates = []
    for i in range(N):
        for j in range(N):
            for k, l in a:
                if i == k or j == l or abs((j - l)/(k - i)) == 1:
                    break
            else:
                candidates.append([i, j])

    return candidates


def backtrack(a, candidates, col: int, N: int):
    """backtrack"""
    if len(a) == N or len(candidates) < len(a):  # finished
        return a
    if len(a) == 0:
        a.append([0, col])
    # if len(candidates) == 0:
    candidates = construct_candidate(a, N)
    next_candidate = candidates[0]
    if next_candidate in candidates:
        a.append(next_candidate)
        return backtrack(a, candidates, col, N)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    if not sys.argv[1].isdigit():
        print('N must be a number')
        exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print('N must be at least 4')
        exit(1)

    for i in range(N):
        solution = backtrack([], [], i, N)
        if len(solution) == N:
            print(solution)

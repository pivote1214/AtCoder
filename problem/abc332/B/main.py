#!/usr/bin/env python3
import sys


def solve(K: int, G: int, M: int):
    glass, mag = 0, 0
    for _ in range(K):
        if glass == G:
            glass = 0
        elif mag == 0:
            mag = M
        else:
            z = min(G - glass, mag)
            glass, mag = glass + z, mag - z
        
    print(glass, mag)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(K, G, M)

if __name__ == '__main__':
    main()

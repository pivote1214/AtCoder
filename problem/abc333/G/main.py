#!/usr/bin/env python3
import sys


def solve(r: float, N: int):


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = float(next(tokens))  # type: float
    N = int(next(tokens))  # type: int
    solve(r, N)

if __name__ == '__main__':
    main()

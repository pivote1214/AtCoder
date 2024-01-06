#!/usr/bin/env python3
import sys


def solve(M: int, D: int, y: int, m: int, d: int):
    if M == m and D == d:
        print(y + 1, 1, 1)
    elif D == d:
        print(y, m + 1, 1)
    else:
        print(y, m, d + 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(M, D, y, m, d)

if __name__ == '__main__':
    main()

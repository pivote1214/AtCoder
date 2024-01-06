#!/usr/bin/env python3
import sys


def solve(N: int, S: int, M: int, L: int):
    ans = 10 ** 10
    for i in range(20):
        for j in range(20):
            for k in range(10):
                if 6 * i + 8 * j + 12 * k >= N:
                    ans = min(ans, i * S + j * M + k * L)

    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, S, M, L)

if __name__ == '__main__':
    main()

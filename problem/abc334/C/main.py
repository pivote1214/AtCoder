#!/usr/bin/env python3
import sys


def solve(N: int, K: int, A: "List[int]"):


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()

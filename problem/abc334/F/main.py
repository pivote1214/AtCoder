#!/usr/bin/env python3
import sys


def solve(N: int, K: int, S_X: int, S_Y: int, X: "List[int]", Y: "List[int]"):


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S_X = int(next(tokens))  # type: int
    S_Y = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, K, S_X, S_Y, X, Y)

if __name__ == '__main__':
    main()

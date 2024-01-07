#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, M: int, A: "List[int]", L: "List[int]", R: "List[int]", X: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    X = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(N, M, A, L, R, X)

if __name__ == '__main__':
    main()

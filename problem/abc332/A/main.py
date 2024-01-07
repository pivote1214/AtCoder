#!/usr/bin/env python3
import sys


def solve(N: int, S: int, K: int, P: list, Q: list):
    ans = 0
    for i in range(N):
        ans += P[i] * Q[i]
    if ans < S:
        ans += K

    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int()] * (N)  # type: "List[int]"
    Q = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        P[i] = int(next(tokens))
        Q[i] = int(next(tokens))
    solve(N, S, K, P, Q)

if __name__ == '__main__':
    main()

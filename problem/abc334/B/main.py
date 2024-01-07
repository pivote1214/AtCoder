#!/usr/bin/env python3
import sys


def solve(A: int, M: int, L: int, R: int):
    L = L - A - 1
    R = R - A

    ans = R // M - L // M
    print(ans)
    
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(A, M, L, R)

if __name__ == '__main__':
    main()

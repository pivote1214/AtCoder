#!/usr/bin/env python3
import sys


def solve(N: int):
    for i in range(N + 1):
        for j in range(N + 1):
            for k in range(N + 1):
                if i + j + k <= N:
                    print(i, j, k)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()

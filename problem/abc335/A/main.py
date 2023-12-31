#!/usr/bin/env python3
import sys


def solve(S: str):
    S = S[:-1] + '4'
    print(S)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()

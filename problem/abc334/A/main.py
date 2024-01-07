#!/usr/bin/env python3
import sys


def solve(B: int, G: int):
    if B > G:
        print("Bat")
    elif B < G:
        print("Glove")
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    B = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    solve(B, G)

if __name__ == '__main__':
    main()

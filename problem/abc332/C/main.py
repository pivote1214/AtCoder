#!/usr/bin/env python3
import sys


def solve(N: int, M: int, S: str):
    ans = 0
    for ss in S.split('0'):
        x, y = 0, 0
        for s in ss:
            if s == '1':
                x += 1
            else:
                y += 1
        x = max(0, x - M)
        ans = max(ans, x + y)
    
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, M, S)

if __name__ == '__main__':
    main()

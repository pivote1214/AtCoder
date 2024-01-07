#!/usr/bin/env python3
import sys


def solve(N: int):
    l = []
    for i in range(1, 15):
        for j in range(1, 15):
            for k in range(1, 15):
                l.append(
                    int('1' * i) + int('1' * j) + int('1' * k)
                )

    l = sorted(list(set(l)))
    ans = l[N - 1]
    print(ans)


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

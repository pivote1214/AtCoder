#!/usr/bin/env python3
import sys


def solve(N: int):
    ans = [[None] * N for _ in range(N)]
    x, y = 0, 0
    dx, dy = 1, 0
    for i in range(1, N * N):
        ans[y][x] = i
        nx, ny = x + dx, y + dy
        if nx < 0 or N <= nx or ny < 0 or N <= ny or ans[ny][nx] is not None:
            dx, dy = -dy, dx
            nx, ny = x + dx, y + dy

        x, y = nx, ny

    ans[y][x] = 'T'

    for row in ans:
        print(*row)


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

#!/usr/bin/env python3

def main():
    N, Q = map(int, input().split())
    l = [(i, 0) for i in range(1, N + 1)]
    l.reverse()
    dir = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    for _ in range(Q):
        n, s = map(str, input().split())
        if n == '1':
            l.append((l[-1][0] + dir[s][0], l[-1][1] + dir[s][1]))
        elif n == '2':
            print(l[-int(s)][0], l[-int(s)][1])
        

if __name__ == '__main__':
    main()

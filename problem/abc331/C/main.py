#!/usr/bin/env python3
import sys
import bisect
from itertools import accumulate

def solve(N: int, A: list):
    A_sorted = sorted(A)
    A_sum = list(accumulate(A_sorted[::-1], initial=0))
    ans = []
    for i in range(N):
        ind = bisect.bisect_right(A_sorted, A[i])
        ans.append(A_sum[N - ind])

    print(*ans)
    
    

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()

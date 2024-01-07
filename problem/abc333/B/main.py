#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    S = input()
    T = input()

    ch_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    s = abs(ch_to_num[S[0]] - ch_to_num[S[1]])
    t = abs(ch_to_num[T[0]] - ch_to_num[T[1]])

    if s == t or s + t == 5:
        print(YES)
    else:
        print(NO)

if __name__ == '__main__':
    main()

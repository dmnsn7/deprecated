#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 100


def main():
    sum_1 = N * (N + 1) // 2
    sum_2 = N * (N + 1) * (2 * N + 1) // 6
    ans = sum_1 * sum_1 - sum_2

    print(ans)


if __name__ == '__main__':
    main()

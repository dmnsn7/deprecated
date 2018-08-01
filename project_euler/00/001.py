#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 1000


def main():
    low_3, high_3 = 3, (N - 1) // 3 * 3
    low_5, high_5 = 5, (N - 1) // 5 * 5
    low_15, high_15 = 15, (N - 1) // 15 * 15

    sum_3 = (low_3 + high_3) * ((high_3 - low_3) // 3 + 1) // 2
    sum_5 = (low_5 + high_5) * ((high_5 - low_5) // 5 + 1) // 2
    sum_15 = (low_15 + high_15) * ((high_15 - low_15) // 15 + 1) // 2

    ans = sum_3 + sum_5 - sum_15

    print(ans)


if __name__ == '__main__':
    main()

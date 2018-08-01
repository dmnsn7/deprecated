#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 20000
M = 500


def get_fac_cnt(num_n):
    fac_cnt = 1
    for i in range(2, num_n + 1):
        if i > num_n // i:
            break
        if num_n % i == 0:
            to_multi = 0
            while num_n % i == 0:
                num_n //= i
                to_multi += 1

            fac_cnt *= to_multi + 1

    if num_n != 1:
        fac_cnt *= 2

    return fac_cnt


def main():
    for i in range(1, N + 1):
        add_up = i * (i + 1) // 2
        if get_fac_cnt(add_up) > M:
            print(add_up)
            break


if __name__ == '__main__':
    main()

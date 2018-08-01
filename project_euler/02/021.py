#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 10000


def get_fac_sum(num_n):
    fac_sum, tmp_n = 1, num_n
    for i in range(2, tmp_n + 1):
        if i > tmp_n // i:
            break
        if tmp_n % i == 0:
            to_multi, base = 1, 1
            while tmp_n % i == 0:
                base *= i
                to_multi += base
                tmp_n //= i
            fac_sum *= to_multi

    if tmp_n != 1:
        fac_sum *= tmp_n + 1

    return fac_sum - num_n


def is_amic(num_n):
    return get_fac_sum(num_n) != num_n and get_fac_sum(
        get_fac_sum(num_n)) == num_n


def main():
    amic_sum = 0
    for i in range(2, N):
        amic_sum += i if is_amic(i) else 0

    print(amic_sum)


if __name__ == '__main__':
    main()

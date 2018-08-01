#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 28123


def get_fac_sum(num_n):
    fac_sum, tmp_n = 1, num_n
    for i in range(2, num_n):
        if i > num_n // i:
            break
        if num_n % i == 0:
            to_multi, base = 1, 1
            while num_n % i == 0:
                base *= i
                to_multi += base
                num_n //= i

            fac_sum *= to_multi

    if num_n != 1:
        fac_sum *= num_n + 1

    return fac_sum - tmp_n


def is_abund(num_n):
    return get_fac_sum(num_n) > num_n


def main():
    abund = set()
    for i in range(1, N + 1):
        if is_abund(i):
            abund.add(i)

    add_up = 0
    for i in range(1, N + 1):
        flag = True
        for num in abund:
            if (num > i - num) or not flag:
                break
            if i - num in abund:
                flag = False
        add_up += i if flag else 0

    print(add_up)


if __name__ == '__main__':
    main()

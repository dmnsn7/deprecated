#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 100


def multiply(vec_a, num_b):
    multi = []
    carry = 0
    for _, dig in enumerate(vec_a):
        tmp = dig * num_b + carry
        multi.append(tmp % 10)
        carry = tmp // 10

    while carry != 0:
        multi.append(carry % 10)
        carry //= 10

    return multi


def main():
    fac = [1]
    for i in range(1, N + 1):
        fac = multiply(fac, i)

    add_up = 0
    for _, dig in enumerate(fac):
        add_up += dig

    print(add_up)


if __name__ == '__main__':
    main()

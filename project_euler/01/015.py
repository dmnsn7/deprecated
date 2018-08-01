#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

R = 20
C = 20


def get_comb(num_a, num_b):
    comb = 1
    for i in range(1, num_b + 1):
        comb = comb * (num_a - i + 1) // i

    return comb


def main():
    comb = get_comb(R + C, R)

    print(comb)


if __name__ == '__main__':
    main()

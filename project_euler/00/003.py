#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 600851475143


def main():
    tmp_n, max_prime_fac, i = N, 0, 2
    while i <= tmp_n // i:
        if tmp_n % i == 0:
            max_prime_fac = i
            while tmp_n % i == 0:
                tmp_n //= i
        i += 1
    if tmp_n != 1:
        max_prime_fac = tmp_n

    print(max_prime_fac)


if __name__ == '__main__':
    main()

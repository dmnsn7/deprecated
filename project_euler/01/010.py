#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 2000000


def prime_sieve(num_n):
    prime = []
    is_prime = [True for i in range(num_n)]
    for i in range(2, num_n):
        if is_prime[i]:
            prime.append(i)
        for _, pri in enumerate(prime):
            if pri * i >= num_n:
                break
            is_prime[pri * i] = False
            if i % pri == 0:
                break

    return prime


def main():
    prime = prime_sieve(N)
    add_up = 0
    for _, pri in enumerate(prime):
        add_up += pri

    print(add_up)


if __name__ == '__main__':
    main()

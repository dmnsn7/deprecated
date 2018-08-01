#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 200000
K = 10001


def prime_sieve(num_n):
    prime = []
    is_prime = [True for i in range(num_n)]
    for i in range(2, num_n):
        if is_prime[i]:
            prime.append(i)
        for num_p in prime:
            if num_p * i >= num_n:
                break
            is_prime[num_p * i] = False
            if i % num_p == 0:
                break

    return prime


def main():
    prime = prime_sieve(N)

    kth_prime = prime[K - 1]

    print(kth_prime)


if __name__ == '__main__':
    main()

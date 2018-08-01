#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

A = 1000
B = 1000
N = 2001000


def prime_sieve(num_n):
    is_prime = [True for _ in range(num_n)]
    prime = set()
    for i in range(2, num_n):
        if is_prime[i]:
            prime.add(i)

        for pri in prime:
            if pri * i >= num_n:
                break
            is_prime[pri * i] = False
            if i % pri == 0:
                break

    return prime


def main():
    prime = prime_sieve(N)
    max_leng, multi = 0, 0
    for i in range(-A + 1, A):
        for j in range(-B + 1, B):
            leng, k = -1, 0
            while leng == -1:
                num = k * k + i * k + j
                if num not in prime:
                    leng = k
                k += 1
            if leng > max_leng:
                max_leng = leng
                multi = i * j

    print(multi)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 10
K = 1000000


def kth_permutation(num_n, num_k):
    fac = [1 for _ in range(num_n)]
    for i in range(1, num_n):
        fac[i] = fac[i - 1] * i

    permutation = []
    is_used = [0 for _ in range(num_n)]
    for i in range(num_n):
        kth = num_k // fac[num_n - i - 1]
        num_k %= fac[num_n - i - 1]
        cnt = 0
        for j in range(num_n):
            cnt += 1 if not is_used[j] else 0
            if cnt == kth + 1:
                permutation.append(j)
                is_used[j] = 1
                break

    return permutation


def main():
    permutation = kth_permutation(N, K - 1)
    for _, dig in enumerate(permutation):
        print(dig, end='')

    print('')


if __name__ == '__main__':
    main()

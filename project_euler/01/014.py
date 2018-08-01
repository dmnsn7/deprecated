#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 1000000

DP = [0 for _ in range(N)]


def dfs(num_n):
    if num_n == 1:
        return 1
    elif num_n < N:
        if DP[num_n] == 0:
            DP[num_n] = dfs(num_n // 2
                            if num_n % 2 == 0 else 3 * num_n + 1) + 1
        return DP[num_n]

    return dfs(num_n // 2 if num_n % 2 == 0 else 3 * num_n + 1) + 1


def main():
    max_length = 1
    target = 1
    for i in range(1, N):
        length = dfs(i)
        if max_length < length:
            max_length = length
            target = i

    print(target)


if __name__ == '__main__':
    main()

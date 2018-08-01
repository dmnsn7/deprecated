#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

D = 1000


def get_recycle_size(num_n):
    remainder = 1
    idx = 1
    visited = {}

    while remainder not in visited:
        visited[remainder], idx = idx, idx + 1

        while remainder != 0 and remainder < num_n:
            remainder *= 10

        remainder %= num_n

    return idx - visited[remainder] if remainder != 0 else 0


def main():
    max_recycle_size, target = 0, 1
    for i in range(1, D):
        if get_recycle_size(i) > max_recycle_size:
            max_recycle_size = get_recycle_size(i)
            target = i

    print(target)


if __name__ == '__main__':
    main()

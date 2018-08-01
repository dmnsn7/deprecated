#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 20


def gcd(num_a, num_b):
    return gcd(num_b, num_a % num_b) if num_b else num_a


def lcm(num_a, num_b):
    return num_a // gcd(num_a, num_b) * num_b


def main():
    ans = 1
    for i in range(1, N + 1):
        ans = lcm(ans, i)

    print(ans)


if __name__ == '__main__':
    main()

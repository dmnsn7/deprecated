#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

LEN = 1000


def add(vec_a, vec_b):
    vec_c = []
    carry = 0
    for i in range(max(len(vec_a), len(vec_b))):
        vec_c.append(carry)
        if i < len(vec_a):
            vec_c[-1] += vec_a[i]
        if i < len(vec_b):
            vec_c[-1] += vec_b[i]
        carry = vec_c[-1] // 10
        vec_c[-1] %= 10

    while carry != 0:
        vec_c.append(carry % 10)
        carry //= 10

    return vec_c


def main():
    idx = 2
    fib_0, fib_1 = [1], [1]
    while len(fib_1) < LEN:
        fib_0, fib_1 = fib_1, add(fib_0, fib_1)
        idx += 1

    print(idx)


if __name__ == '__main__':
    main()

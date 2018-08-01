#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

D = 4000000


def main():
    fib = [1, 2]
    while fib[-2] + fib[-1] <= D:
        fib.append(fib[-2] + fib[-1])

    sum_up = 0
    for i, _ in enumerate(fib):
        if fib[i] % 2 == 0:
            sum_up += fib[i]

    print(sum_up)


if __name__ == '__main__':
    main()

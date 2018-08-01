#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''


def is_palin(num):
    digit = []
    while num != 0:
        digit.append(num % 10)
        num //= 10
    for i, _ in enumerate(digit):
        if digit[i] != digit[-1 - i]:
            return False

    return True


def main():
    max_palin = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            multi = i * j
            if multi > max_palin and is_palin(multi):
                max_palin = multi

    print(max_palin)


if __name__ == '__main__':
    main()

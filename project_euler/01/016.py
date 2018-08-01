#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 1000


def multi_2(num_s):
    num_t = ''
    carry = 0
    for _, cha in enumerate(num_s):
        digit = carry + int(cha) * 2
        num_t += str(digit % 10)
        carry = digit // 10

    if carry != 0:
        num_t += str(carry)

    return num_t


def main():
    num = '1'
    for _ in range(N):
        num = multi_2(num)

    add_up = 0
    for _, dig in enumerate(num):
        add_up += int(dig)

    print(add_up)


if __name__ == '__main__':
    main()

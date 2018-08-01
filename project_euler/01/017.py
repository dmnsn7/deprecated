#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 1000

ZERO_TO_NINETEEN = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

ZERO_TO_NINETY = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

HUNDRED = 'hundred'
AND = 'and'
THOUSAND = 'thousand'


def get_cnt(num_n):
    if num_n <= 19:
        return len(ZERO_TO_NINETEEN[num_n])
    elif num_n <= 99:
        return len(ZERO_TO_NINETY[num_n // 10]) + len(
            ZERO_TO_NINETEEN[num_n % 10])
    elif num_n <= 999:
        return len(ZERO_TO_NINETEEN[num_n // 100]) + len(HUNDRED) + (
            len(AND) + get_cnt(num_n % 100) if num_n % 100 != 0 else 0)

    return len(ZERO_TO_NINETEEN[1]) + len(THOUSAND)


def main():
    add_up = 0
    for i in range(1, 1001):
        add_up += get_cnt(i)

    print(add_up)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

YEAR_BEGIN = 1900
YEAR_END = 2000

MONTH_DAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


def main():
    year, month, week = YEAR_BEGIN, 0, 1
    cnt = 0
    while year <= YEAR_END:
        cnt += 1 if year >= YEAR_BEGIN + 1 and week == 0 else 0
        week = (week + MONTH_DAY[month] + (month == 1 and is_leap(year))) % 7
        year += 1 if month == 11 else 0
        month = 0 if month == 11 else month + 1

    print(cnt)


if __name__ == '__main__':
    main()

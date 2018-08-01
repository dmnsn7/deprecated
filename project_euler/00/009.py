#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

SUM = 1000


def main():
    for i in range(1, SUM + 1):
        for j in range(i, SUM - i + 1):
            if SUM - i - j < j:
                break
            k = SUM - i - j
            if i * i + j * j == k * k:
                multi = i * j * k
                print(multi)


if __name__ == '__main__':
    main()

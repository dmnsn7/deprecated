#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''


def main():
    text = input()
    names = text.split(',')

    for i, _ in enumerate(names):
        names[i] = names[i][1:-1]

    names = sorted(names)

    score_sum = 0
    for i, name in enumerate(names):
        for _, cha in enumerate(name):
            score_sum += (ord(cha) - ord('A') + 1) * (i + 1)

    print(score_sum)


if __name__ == '__main__':
    main()

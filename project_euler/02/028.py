#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 1001


def main():
    vec = [1, 24, 52, 32]
    for _ in range(N // 2):
        vec = [vec[0] + vec[1], vec[1] + vec[2], vec[2] + vec[3], vec[3]]

    print(vec[0])


if __name__ == '__main__':
    main()

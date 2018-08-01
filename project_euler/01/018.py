#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

N = 15

GRID = [
    "75",
    "95 64",
    "17 47 82",
    "18 35 87 10",
    "20 04 82 47 65",
    "19 01 23 75 03 34",
    "88 02 77 73 07 63 67",
    "99 65 04 28 06 16 70 92",
    "41 41 26 56 83 40 80 70 33",
    "41 48 72 33 47 32 37 16 94 29",
    "53 71 44 65 25 43 91 52 97 51 14",
    "70 11 33 28 77 73 17 78 39 68 17 57",
    "91 71 52 38 17 14 91 43 58 50 27 29 48",
    "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
    "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23",
]


def main():
    max_sum = 0
    dp_pre = []
    for i in range(N):
        dp_cur = [0 for _ in range(i + 1)]
        for j in range(i + 1):
            num = int(GRID[i].split()[j])
            if i == 0:
                dp_cur[j] = num
            elif j == 0:
                dp_cur[j] = dp_pre[j] + num
            elif i == j:
                dp_cur[j] = dp_pre[j - 1] + num
            else:
                dp_cur[j] = max(dp_pre[j], dp_pre[j - 1]) + num

            max_sum = max(max_sum, dp_cur[j])

        dp_pre = dp_cur

    print(max_sum)


if __name__ == '__main__':
    main()

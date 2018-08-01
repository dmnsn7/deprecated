#!/usr/bin/env python3
'''Copyright [2017] <dmnsn7@gmail.com>'''

A = 100
B = 100


def main():
    is_visited = set()
    cnt = (A - 1) * (B - 1)
    for i in range(2, A + 1):
        for j in range(2, B + 1):
            tmp_i, min_div = i, 1
            for k in range(2, tmp_i + 1):
                if k > tmp_i / k:
                    break
                if tmp_i % k == 0:
                    min_div *= k
                    while tmp_i % k == 0:
                        tmp_i /= k

            tmp_tmp_i, level = i, 0
            while min_div != 1 and tmp_tmp_i % min_div == 0:
                tmp_tmp_i /= min_div
                level += 1

            if tmp_tmp_i != 1:
                is_visited.add((i, j))
            elif (min_div, level * j) not in is_visited:
                is_visited.add((min_div, level * j))
            else:
                cnt -= 1

    print(cnt)


if __name__ == '__main__':
    main()

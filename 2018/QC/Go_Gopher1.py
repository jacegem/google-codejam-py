# QC

import sys


# def get_req(cell):
#     for i in range(3 + 3, 998 + 998 + 1):
#         for j in range(3, i - 3):
#             k = i - j
#             # I use j, k
#             if cell[j][k] is 0:
#                 return j, k, cell

def get_req(cell, cell_map, idx):
    while True:
        idx = idx % len(cell_map)
        j, k = cell_map[idx]
        if cell[j][k] is 0:
            return j, k, cell
        else:
            idx += 1


def main_submit():
    t = int(input())  # read a line with a single integer

    for i in range(t):
        a = int(input())

        w = h = a
        cell = [[0 for x in range(w)] for y in range(h)]
        cell_map = {}

        idx = 0
        w = h = int(a / 2) + 1
        for ci in range(3 + 3, w + h + 1):
            for cj in range(3, ci - 2):
                ck = ci - cj
                cell_map[idx] = [cj, ck]
                idx += 1

        idx = 0
        done = False

        while done is False:
            req_x, req_y, cell = get_req(cell, cell_map, idx)
            print("{} {}".format(req_x, req_y))
            x, y = sys.stdin.read().strip().split(" ")

            sys.stderr.write('req:{} {}, receive:{} {}\n'.format(req_x, req_y, x, y))
            if x is 0 and y is 0:
                done = True
            elif x is -1 and y is -1:
                break

            cell[int(x)][int(y)] = 1
            idx += 1


            # # sys.stdout.flush()
            # # x = input()
            # y = int(input())
            # print("{} {}".format(x, y))


def test():
    t = int(input())  # read a line with a single integer
    a = int(input())

    for i in range(2, 1000):
        print("{} {}".format(i, i))
        x, y = sys.stdin.read().strip().split(" ")
        sum = x + y


if __name__ == "__main__":
    main_submit()

"""
2
5
5 6 8 4 3
3
8 9 7
"""

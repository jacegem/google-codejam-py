import numpy as np


def read_line():
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line


def read_int():
    r = read_line()
    return int(r)


def main_solve():
    for case in range(read_int()):
        N = read_int()
        M = np.array([list(map(int, read_line().split())) for _ in range(N)])

        K = np.trace(M)
        R = sum(len(set(r)) < N for r in M)
        C = sum(len(set(r)) < N for r in M.T)
        print(f'Case #{case + 1}: {K} {R} {C}')


use_sample = True
input_file = None

if __name__ == "__main__":
    try:
        if use_sample is True:
            input_file = open('input.txt2', "r")
    except FileNotFoundError as e:
        pass

    main_solve()

    if input_file:
        input_file.close()

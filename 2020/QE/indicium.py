"""
## Problem

Indicium means "trace" in Latin. In this problem we work with Latin squares and
matrix traces.

A Latin square is an N-by-N square matrix in which each cell contains one of N
different values, such that no value is repeated within a row or a column. In this
problem, we will deal only with "natural Latin squares" in which the N values are
the integers between 1 and N.

The trace of a square matrix is the sum of the values on the main diagonal
(which runs from the upper left to the lower right).

Given values N and K, produce any N-by-N "natural Lating square" with trace K, or
say it is impossible. For example, here are two possible answers for N=3, K=6.
In each case, the values that contribute to the trace are underlined.



"""


def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()


def main_solve():
    t = int(read_line())

    for case in range(t):
        n, k = map(int, read_line().split())

        answer = "IMPOSSIBLE"

        for i in range(1, n + 1):
            if k == i * n:
                answer = "POSSIBLE"
                break

        print('Case #{}: {}'.format(case + 1, answer))


use_sample = True
input_file = None

if __name__ == "__main__":
    try:
        if use_sample is True:
            input_file = open('input.txt', "r")
    except FileNotFoundError as e:
        pass

    main_solve()

    if input_file:
        input_file.close()

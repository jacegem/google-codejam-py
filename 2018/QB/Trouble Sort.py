# QB
def tsort(n, vs):
    while True:
        before = vs[:]
        for i in range(n - 2):
            if vs[i] > vs[i + 2]:
                vs[i], vs[i + 2] = vs[i + 2], vs[i]

        if vs == before:
            return vs


def solve(n, vs):
    tsorted = tsort(n, vs)

    for i in range(n - 1):
        if tsorted[i] > tsorted[i+1]:
            return i

    return 'OK'


def main_submit():
    test_case = int(input())  # read a line with a single integer
    for case in range(1, test_case + 1):
        n = int(input())
        vs = [int(s) for s in input().split(" ")]
        answer = solve(n, vs)
        result = 'Case #{}: {}'.format(case, answer)
        print(result)


if __name__ == "__main__":
    main_submit()

"""
2
5
5 6 8 4 3
3
8 9 7
"""

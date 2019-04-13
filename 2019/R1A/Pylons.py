



def find_exit(galaxy, path_list, rlen, clen):
    # print(galaxy)

    # 모든 곳을 다 갔는가?
    # 그러면 possible
    if len(path_list) >= rlen * clen:
        return path_list

    # 다음 갈 곳을 찾는다.
    for r in range(rlen):
        for c in range(clen):
            # 갈 수 있는가?
            if galaxy[r][c] is True:
                continue

            lr, lc = path_list[-1]
            if r != lr and c != lc and r + c != lr + lc and r - c != lr-lc:
                galaxy[r][c] = True
                path_list.append([r, c])
                rst = find_exit(galaxy, path_list, rlen, clen)

                if rst is not None:
                    return path_list

    return None


def solve(rlen, clen):
    for r in range(rlen):
        for c in range(clen):
            galaxy = [[False for _ in range(clen)] for _ in range(rlen)]
            path_list = [[r, c]]

            galaxy[r][c] = True
            rst = find_exit(galaxy.copy(), path_list, rlen, clen)
            if rst is not None:
                return rst

    return None


def main_submit():
    test_case = int(read_line())

    for case in range(1, test_case + 1):
        r, c = [int(s) for s in read_line().split(" ")]  # read a list of integers, 2 in this case
        result_list = solve(r,c)

        if result_list is None:
            answer = 'IMPOSSIBLE'
        else:
            answer = 'POSSIBLE'

        result = 'Case #{}: {}'.format(case, answer)
        print(result)

        if result_list is not None:
            for r,c in result_list:
                print('{} {}'.format(r+1, c+1))



def read_line():
    if isLocal is True:
        line = inp_file.readline()
    else:
        line = input()

    return line.strip()


isLocal = True
inp_file = ''

if __name__ == "__main__":
    if isLocal is True:
        inp_file = open('input_file.txt', "r")

    main_submit()

# Problem C
import math




def matrix_append(matrix, cnt, str):
    if cnt > 0:
        for i in range(cnt):
            matrix.append([str, None])
    return matrix


def make_place(place, matrix):
    last = place[-1]
    # 가능한 다음 변수 찾기
    all_used = True

    for i in range(len(matrix)):
        color = matrix[i][0]
        used = matrix[i][1]

        if used:
            continue
        all_used = False

        if last is 'R' and color in ('R', 'O', 'V'):
            continue
        if last is 'Y' and color in ('Y', 'O', 'G'):
            continue
        if last is 'O' and color in ('R', 'Y', 'O', 'G', 'V'):
            continue
        if last is 'B' and color in ('B', 'G', 'V'):
            continue
        if last is 'G' and color in ('G', 'O', 'V', 'Y', 'B'):
            continue
        if last is 'V' and color in ('V', 'R', 'B', 'O', 'G'):
            continue

        matrix[i][1] = True
        place.append(color)
        result = make_place(place, matrix)
        if result is None:
            place.pop()
            matrix[i][1] = None
        else:
            place = result

    # 모두 사용하였는가
    for i in range(len(matrix)):
        used = matrix[i][1]
        if used is None:
            return None

    first = place[1]
    last = place[-1]
    if last is 'R' and first in ('R', 'O', 'V'):
        return None
    if last is 'Y' and first in ('Y', 'O', 'G'):
        return None
    if last is 'O' and first in ('R', 'Y', 'O', 'G', 'V'):
        return None
    if last is 'B' and first in ('B', 'G', 'V'):
        return None
    if last is 'G' and first in ('G', 'O', 'V', 'Y', 'B'):
        return None
    if last is 'V' and first in ('V', 'R', 'B', 'O', 'G'):
        return None
    return place


def main():
    inputFile = 'B-small-attemp.in'
    # inputFile = 'A-large.in'
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    for case in range(test_case):

        n, r, o, y, g, b, v = [int(x) for x in inpf.readline().strip().split(' ')]

        matrix = []
        matrix = matrix_append(matrix, r, 'R')
        matrix = matrix_append(matrix, o, 'O')
        matrix = matrix_append(matrix, y, 'Y')
        matrix = matrix_append(matrix, g, 'G')
        matrix = matrix_append(matrix, b, 'B')
        matrix = matrix_append(matrix, v, 'V')

        place = []
        place.append(matrix[0][0])
        matrix[0][1] = True
        place = make_place(place, matrix)

        result = 'IMPOSSIBLE'
        if place is not None:
            result = ''.join(place)
        result = 'Case #{}: {}\n'.format(case + 1, result)
        print(result, end='')
        outf.write(result)

    inpf.close()
    outf.close()


if __name__ == "__main__":
    main()

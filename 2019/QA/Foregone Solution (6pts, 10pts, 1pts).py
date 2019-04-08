def find_ab(n):
    s = str(n)
    # r = s[::-1]
    l = len(s)
    a = []
    b = []

    # print('length:', l)

    for i in range(0, l):
        if s[i] == '4':
            a.append('2')
            b.append('2')
        else:
            a.append(s[i])
            b.append('0')

    return int(''.join(a)), int(''.join(b))


def read_line():
    if isLocal is True:
        line = inp_file.readline()
    else:
        line = input()

    return line


def main_submit():
    test_case = int(read_line())

    for case in range(1, test_case + 1):
        n = int(read_line())
        a, b = find_ab(n)
        result = 'Case #{}: {} {}'.format(case, a, b)
        print(result)


isLocal = False
inp_file = ''

if __name__ == "__main__":
    if isLocal is True:
        inp_file = open('input_file.txt', "r")

    main_submit()


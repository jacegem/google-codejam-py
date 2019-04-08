SOUTH = 'S'
EAST = 'E'


def get_cnt(target, stop):
    s_cnt = 0
    e_cnt = 0

    for i in range(stop):
        if target[i] == SOUTH:
            s_cnt += 1
        else:
            e_cnt += 1

    return s_cnt, e_cnt


# def find_path(n, path):
#     root = []
#
#     for i in range(len(path)):
#         if i == 0:
#             if path[i] == SOUTH:
#                 root.append(EAST)
#             else:
#                 root.append(SOUTH)
#         else:
#             path_s_cnt, path_e_cnt = get_cnt(path, i)
#             root_s_cnt, root_e_cnt = get_cnt(root, i)
#
#             if path_s_cnt > root_s_cnt:
#                 root.append(SOUTH)
#             elif path_e_cnt > root_e_cnt:
#                 root.append(EAST)
#             else:
#                 if path[i] == SOUTH:
#                     root.append(EAST)
#                 else:
#                     root.append(SOUTH)
#
#     return root

def find_root(path):
    root = []
    for i in range(len(path)):
        if path[i] == SOUTH:
            root.append(EAST)
        else:
            root.append(SOUTH)

    return root


def main_submit():
    test_case = int(read_line())

    for case in range(1, test_case + 1):
        n = int(read_line())
        path = read_line()

        route = find_root(path)
        result = 'Case #{}: {}'.format(case, ''.join(route))
        print(result)


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

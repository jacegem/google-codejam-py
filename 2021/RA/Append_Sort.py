def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()


def main_solve():
    t = int(read_line())

    for case in range(t):
        n = int(read_line())
        x_list = read_line().split()

        app = 0

        for i in range(1, len(x_list)):
            before = x_list[i - 1]
            current = x_list[i]

            if int(before) >= int(current):
                cur_len = len(current)
                before_tail = before[cur_len:]

                before_nine = '9' * len(before_tail)

                # 9999... 를 붙여서 되는가 ?
                if int(before) < int(current + before_nine):

                    # 0000... 를 붙여서 되는가?
                    before_zero = '0' * len(before_tail)
                    if int(before) < int(current + before_zero):
                        before_tail = before_zero
                    else:
                        for tail_idx in range(len(before_tail) - 1, -1, -1):
                            last = before_tail[tail_idx]
                            if last == '9':
                                before_tail[tail_idx] = '0'
                            else:
                                # before_tail[tail_idx] = str(int(last) + 1)
                                before_tail = before_tail[:tail_idx] + str(int(last) + 1) + before_tail[tail_idx + 1:]
                                break
                # 안되면 000
                else:
                    before_tail = '0' * (len(before_tail) + 1)

                app += len(before_tail)
                x_list[i] = current + before_tail
                # print(before, x_list[i])

        print(f'Case #{case + 1}: {app}')


use_sample = True
input_file = None

if __name__ == "__main__":
    try:
        if use_sample is True:
            input_file = open('append_sort.txt', "r")
    except FileNotFoundError as e:
        pass

    main_solve()

    if input_file:
        input_file.close()

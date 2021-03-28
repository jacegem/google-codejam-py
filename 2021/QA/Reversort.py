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
        src_list = list(map(int, read_line().split()))

        total_cost = 0

        for idx in range(n - 1):
            min_val = min(src_list[idx:])
            target_idx = src_list.index(min_val)
            src_list[idx:target_idx + 1] = list(reversed(src_list[idx:target_idx + 1]))

            cost = target_idx - idx + 1
            total_cost += cost

        print('Case #{}: {}'.format(case + 1, total_cost))


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

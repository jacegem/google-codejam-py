def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()


def get_list2(n, c):
    src_list = list(range(1, n + 1))
    last_idx = len(src_list) - 1

    for idx in range(last_idx - 1, -1, -1):
        max_cost = last_idx - idx + 1
        remain_cost = idx
        usable_cost = c - remain_cost

        if usable_cost >= max_cost:
            src_list[idx: last_idx + 1] = list(reversed(src_list[idx:last_idx + 1]))
            c -= max_cost
        elif usable_cost == 1:
            c -= 1
        else:
            target_idx = idx + usable_cost + 1
            src_list[idx: target_idx] = list(reversed(src_list[idx:target_idx]))
            c = c - (target_idx - idx + 1)
        if c == 0:
            return src_list

    return src_list


def get_list(n, c):
    src_list = list(range(1, n + 1))

    last_idx = len(src_list) - 1

    for idx in range(len(src_list) - 1):

        max_cost = last_idx - idx + 1
        remain_cost = last_idx - idx

        usable_cost = c - remain_cost

        if usable_cost >= max_cost:
            src_list[idx: last_idx + 1] = list(reversed(src_list[idx:last_idx + 1]))
            c -= max_cost
        elif usable_cost == 1:
            c -= 1
        else:
            target_idx = idx + usable_cost + 1
            src_list[idx: target_idx] = list(reversed(src_list[idx:target_idx]))
            c = c - (target_idx - idx + 1)

        if c == 0:
            return src_list

    return src_list


def main_solve():
    t = int(read_line())

    for case in range(t):
        n, c = list(map(int, read_line().split()))

        if c < n - 1 or n * (n + 1) / 2 -1 < c:
            result = "IMPOSSIBLE"
        else:
            result = get_list2(n, c)
            result = " ".join(map(str, result))

        print(f'Case #{case + 1}: {result}')


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

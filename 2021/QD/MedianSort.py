def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()


def main_solve():
    t = int(read_line())

    for case in range(t):
        p = int(read_line())

        for i in range(100):
            answer = list(map(int, list(read_line())))
            ans_sum = sum(answer)

            print(ans_sum)

        print(f'Case #{case + 1}: {p}')


use_sample = True
input_file = None

if __name__ == "__main__":
    try:
        if use_sample is True:
            input_file = open('../QE/input.txt', "r")
    except FileNotFoundError as e:
        pass

    main_solve()

    if input_file:
        input_file.close()

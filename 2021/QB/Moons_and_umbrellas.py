def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()


def visible_case(x, y, s):
    first = "!"
    for v in s:
        if v == "C" or v == "J":
            first = v
            break

    for idx in range(len(s)):
        v = s[idx]
        if v == "?":
            s[idx] = first
        else:
            first = s[idx]

    return s


def hidden_case(x, y, s):
    # CJ
    # 앞이 C 이면 다음은 J
    """
    C -> J
    J -> ?? -> CJ
    J -> ?C -> JC, CC
    J -> ?J -> CJ
    J -> ?  ->
    """
    if x <= y:
        first = "C"
    else:
        first = "J"

    min_x = (x <= y)
    minus_x = (x < 0)
    minus_y = (y < 0)

    for idx in range(len(s)):
        val = s[idx]

        if idx == 0 and val == "?":
            s[idx] = first
            continue

        if val == "?":
            if first == "C":
                if minus_x:
                    s[idx] = "J"
                else:
                    s[idx] = "C"
            else:
                if minus_y:
                    s[idx] = "C"
                else:
                    s[idx] = "J"

        first = s[idx]

    return s


def get_cost(x, y, s):
    ## cost
    total_cost = 0
    for idx in range(len(s) - 1):
        if s[idx:idx + 2] == list("CJ"):
            total_cost += x
        if s[idx:idx + 2] == list("JC"):
            total_cost += y

    return total_cost


def main_solve():
    t = int(read_line())

    for case in range(t):
        x, y, s = read_line().split()
        x = int(x)
        y = int(y)
        s = list(s)

        if min(x, y) < 0:
            make_minus = True
            s = hidden_case(x, y, s)
        else:
            s = visible_case(x, y, s)

        total_cost = get_cost(x, y, s)

        print(f'Case #{case + 1}: {total_cost}')


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

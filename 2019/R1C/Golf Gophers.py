def solve(word_list, accent_list):
    word_len = len(word_list)
    max_len = len(accent_list) * 2

    if word_len < 2:
        return max_len

    for f_idx in range(word_len):
        for s_idx in range(word_len):
            if f_idx >= s_idx:
                continue

            f_word = word_list[f_idx]
            s_word = word_list[s_idx]

            word_list_copy = word_list.copy()
            word_list_copy.remove(f_word)
            word_list_copy.remove(s_word)

            f_len = len(f_word)
            s_len = len(s_word)
            min_len = min(f_len, s_len)



            for i in range(min_len):

                f_rhyme = f_word[f_len - min_len + i:]
                s_rhyme = s_word[s_len - min_len + i:]
                accent = f_word[f_len - min_len + i]

                if f_rhyme == s_rhyme and accent not in accent_list:
                    accent_list_copy = accent_list.copy()

                    accent_list_copy.append(accent)
                    rst = solve(word_list_copy, accent_list_copy)

                    max_len = max(max_len, rst)

    # print(max_len)
    return max_len


def main_submit():
    test_case = int(read_line())

    for case in range(1, test_case + 1):
        count = int(read_line())

        word_list = []
        for c in range(count):
            word = read_line()
            word_list.append(word)

        result = solve(word_list, [])

        result = 'Case #{}: {}'.format(case, result)
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

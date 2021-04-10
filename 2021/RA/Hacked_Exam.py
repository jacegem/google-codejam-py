def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()


def gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대입
        x, y = y, x % y
    return x


def main_solve():
    t = int(read_line())

    for case in range(t):
        n, q = list(map(int, read_line().split()))

        answer_list = []
        score_list = []

        for i in range(n):
            answer, score = list(read_line().split())
            answer_list.append(answer)
            score_list.append(score)

        y_list = []
        max_score = 0

        for col in range(q):
            p_t = 0
            p_f = 0
            for row in range(len(answer_list)):
                answer = answer_list[row][col]
                score = score_list[row]

                p = int(score)

                if answer == 'T':
                    p_t += p
                    p_f += q - p
                else:
                    p_t += q - p
                    p_f += p

            if p_t > p_f:
                y_list.append('T')
                max_score += 1
            elif p_f > p_t:
                y_list.append('F')
                max_score += 1
            else:
                y_list.append('F')

        # max_score = max_p / q / n

        for row in range(len(score_list)):
            score = int(score_list[row])

            if score > max_score:
                max_score = score
                y_list = answer_list[row]

        print(f'Case #{case + 1}: {"".join(y_list)} {int(max_score)}/1')
        # r = q * n
        # g = gcd(max_score, r)
        #
        # print(f'Case #{case + 1}: {"".join(y_list)} {int(max_score / g)}/{int(r / g)}')


use_sample = True
input_file = None

if __name__ == "__main__":
    try:
        if use_sample is True:
            input_file = open('hacked_exam.txt', "r")
    except FileNotFoundError as e:
        pass

    main_solve()

    if input_file:
        input_file.close()

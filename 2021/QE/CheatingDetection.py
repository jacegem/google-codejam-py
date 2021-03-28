from collections import namedtuple

import numpy as np


def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()


Activity = namedtuple("Activity", ["sum", "arr"])

Problem = namedtuple("Problem", ["id", "prop"])
Skill = namedtuple("Skill", ["id", "prop"])


def main_solve3():
    t = int(read_line())
    p = int(read_line())

    for case in range(t):
        skill_list = []
        ans_list = []
        for i in range(100):
            answer = list(map(int, list(read_line())))
            ans_list.append(answer)
            p = np.mean(answer)
            skill_list.append(Skill(i, p))

        arr = np.array(ans_list)
        arr_t = arr.T
        problem_list = []
        for idx, a in enumerate(arr_t):
            p = np.mean(a)
            problem_list.append(Problem(idx, p))

        problem_list.sort(key=lambda x: x.prop)

        base_p = 0.2
        cheat_count_list = [0] * 100
        for problem in problem_list:
            # 문제의 정답 확률

            prob_p = problem.prop

            if prob_p > base_p:
                continue

            col_idx = problem.id

            for skill in skill_list:
                skill_p = skill.prop
                row_idx = skill.id

                ans = ans_list[row_idx][col_idx]
                sum_p = prob_p + skill_p

                if ans == 1 and sum_p < 0.3:
                    cheat_count_list[row_idx] += ((1 - prob_p) + (1 - skill_p))

                # if ans == 1 and sum_p < 0.5:
                #     # cheat_count_list[row_idx] += (base_p - prob_p)
                #     cheat_count_list[row_idx] += (0.5 - sum_p)

        # print(cheat_count_list)
        max_cheat = max(cheat_count_list)
        cheat_idx = cheat_count_list.index(max_cheat)
        print(f'Case #{case + 1}: {cheat_idx + 1}')


def main_solve2():
    t = int(read_line())
    p = int(read_line())

    for case in range(t):

        ans_list = []
        for i in range(100):
            answer = list(map(int, list(read_line())))
            ans_list.append(answer)

        arr = np.array(ans_list)
        arr_t = arr.T

        act_list = []
        for a in arr_t:
            sum_a = sum(a)
            act = Activity(sum_a, a)
            act_list.append(act)
            # if sum_a < 50:
            #     cheat_list.append(a)

        act_list.sort(key=lambda x: x.sum)

        cheat_list = []
        for act in act_list[:100]:
            cheat_list.append(act.arr)

        arr = np.array(cheat_list)
        arr_t = arr.T

        cheat_point = []
        for a in arr_t:
            cheat_point.append(sum(a))

        max_point = max(cheat_point)
        cheat_idx = cheat_point.index(max_point)

        print(f'Case #{case + 1}: {cheat_idx + 1}')


def main_solve():
    t = int(read_line())
    p = int(read_line())

    for case in range(t):

        """
        10% 의 의미
        86% 의 의미
        """
        ans_list = []

        for i in range(100):
            answer = list(map(int, list(read_line())))
            ans_sum = sum(answer)

            ans_list.append(ans_sum)
            # print(f"ans_sum: {ans_sum}")

        max_ans = max(ans_list)
        # print(f"max: {max_ans}")

        max_idx = ans_list.index(max_ans)
        # print(f"max idx : {max_idx}")

        # ans_mean = sum(ans_list) / 100
        # print(f"ans_mean: {ans_mean}")

        # filter(lambda u: u["sex"] != "M", users)
        # filter_list = list(filter(lambda x: x > ans_mean, ans_list))
        # filter_list = list(filter(lambda x: x >= 5000, ans_list))
        # result = len(filter_list)
        # print(f"filter count: result")

        print(f'Case #{case + 1}: {max_idx + 1}')


use_sample = True
input_file = None

if __name__ == "__main__":
    try:
        if use_sample is True:
            input_file = open('input.txt', "r")
    except FileNotFoundError as e:
        pass

    main_solve3()

    if input_file:
        input_file.close()

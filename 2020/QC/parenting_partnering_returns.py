"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9


# Parenting Partnering Returns

## Problem

Cameraon and Jamie's kid is almost 3 years old! However, evne though the child
is more independent now, scheduling kid activites and domestic necessities is
still a challenge for the couple.

Cameron and Jamie have a list of N activities to take care of during the day.
Each activity happens during a specified interval during the day. They need to
assign each activity to one of them, so that neither of them is responsible for
two activities that overlap. An activity that ends at time t is not considered to
overlap with another activity that start at time t.

For example, suppose that Jamie and Cameron need to cover 3 activites; one
running from 18:00 to 20:00, another from 19:00 to 21:00 and another from
22:00 to 23:00. One possibility would be for Jamie to cover the activity running
from 19:00 to 21:00, with Cameron covering the other two. Another valid
schedule would be fore Cameron to cover the activity from 18:00 to 20:00 and
Jamie to cover the other two. Notice taht the first two activities overlap in the
time between 19:00 and 20:00, so it is impossible to assign both of those
activities to the same partner.

Given the starting and ending times of each activity, find any schedule that does
not require the same person to cover overlapping activities, or say that it is
impossible.

## Input

The first line of the input gives the number of test cases, T. T test cases follow.
Each test case starts with a line containing a single integer N,


# Codejam 2020, Qualification Round: Parenting Partnering Returns
# https://github.com/theXYZT/codejam-2020/blob/master/Qualification%20Round/parenting-partnering-returns.py


from collections import namedtuple

Activity = namedtuple("Activity", ["id", "start", "end"])

# I/O Code
num_cases = int(input())
for case in range(1, num_cases + 1):
    N = int(input())

    activities = []
    for i in range(N):
        a, b = map(int, input().split())
        activities.append(Activity(i, a, b))
    activities.sort(key=lambda x: x.start)

    C, J = 0, 0
    assignments = ['*'] * N
    for a in activities:
        if C <= a.start:
            assignments[a.id] = 'C'
            C = a.end
        elif J <= a.start:
            assignments[a.id] = 'J'
            J = a.end
        else:
            break

    result = "".join(assignments)

    if '*' in result:
        print('Case #{}: IMPOSSIBLE'.format(case))
    else:
        print('Case #{}: {}'.format(case, result))
"""
from collections import namedtuple

Activity = namedtuple("Activity", ["id", "start", "end"])


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

        activities = []

        for i in range(n):
            start, end = map(int, read_line().split())
            activities.append(Activity(i, start, end))

        activities.sort(key=lambda x: x.start)

        C, J = 0, 0
        assignment = ['*'] * n

        for a in activities:
            if a.start >= C:
                assignment[a.id] = 'C'
                C = a.end
            elif a.start >= J:
                assignment[a.id] = 'J'
                J = a.end
            else:
                break

        if '*' in assignment:
            result = "IMPOSSIBLE"
        else:
            result = ''.join(assignment)

        print('Case #{}: {}'.format(case + 1, result))


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

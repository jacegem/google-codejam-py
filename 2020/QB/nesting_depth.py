"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

# Nesting Depth

## Problem

tl;dr: Given a String of digits S, insert a minium number of opening and closing parentheses
into it such that the resulting string is balanced and each digit d is inside exactly d pairs
of matching parentheses.

Let the nesting of two parentheses within a string be the substring that occurs strictly
between them. An opening parenthesis and a closing parenthesis that is further to its right
are said to match if their nesting is empty, or if every parenthesis in their nesting matches
with another parenthesis in their nesting. The nesting depth of a position p is the number of
pairs of matching parentheses m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth:
0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1).
The first three strings have minimum length among those that have the same digits in the same order,
but the last one does not since ((22)1) also has the digits 221 and is shorter.

Given a string of digits S, find another string S', comprised of parentheses and digits, such that:
- all parentheses in S' match some other parenthesis,
- removing any and all parentheses from S' results in S,
- each digit in S' is equal to its nesting depth, and
- S' is of minimum length.

## Input

The first line of the input gives the number of test cases, T.
T lines follow. Each line represents a test case and contains
only the string S.

## Output

For each test case, output one line containing Case #x: y, where x is the test case
number (starting from 1) and y is the string S' defined above.

"""
from typing import List





def read_int() -> int:
    r = read_line()
    return int(r)


def read_int_list() -> List[int]:
    r = read_line()
    int_list = list(map(int, r[:]))
    return int_list


def main_solve():
    t = read_int()

    for case in range(t):
        s = read_int_list()

        result = ""
        p_count = 0

        for number in s:
            while number > p_count:
                result += "("
                p_count += 1

            while number < p_count:
                result += ")"
                p_count -= 1

            result += str(number)

        while p_count > 0:
            result += ")"
            p_count -= 1

        print(f'Case #{case + 1}: {result}')


def read_line() -> str:
    if input_file:
        line = input_file.readline()
    else:
        line = input()

    return line.strip()

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

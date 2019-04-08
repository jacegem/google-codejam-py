#!/usr/bin/env python

inputFile = 'A-small.in'
outFile = inputFile + ".out"
outf = open(outFile, "w")

def solve():
    a = input()
    print('aa')


test_case = int(input())
outf.write('hey {}'.format(test_case))

for _ in range(test_case):
    solve()



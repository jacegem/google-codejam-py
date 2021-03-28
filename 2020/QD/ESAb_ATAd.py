"""
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e

## Problem

Last year, a research consortitum had some trouble with a distributed database
system that sometimes lost pieces of the data. You do not need to read or
understand that problem in order to solve this one!

The consortitum has decided that distributed systems are too complicated, so
they are storing B bits of important information in a single array on one
awesome machine. As an additional layer of security, they have made it difficult
to obtain the information quickly; the user must query for a bit position between
1 and B, and then they receive that bit of the stored array as a response.

Unfortunately, this ultra-modern machine is subject to random quantum
fluctuations! Specifically, after every 1st, 11th, 21st, 31st... etc. query is sent, but
before the response is given, quantum fluctuation causes exactly one of the
following four effects, with equal probability:

- 25% of the time, the array is complemented: every 0 becomes a 1, and vice versa.
- 25% of the time, the array is reversed: the first bit swaps with the last bit,
the second bit swaps with the second-to-last bit, and so on.
- 25% of the time, both of the things above (complementation and reversal)
happend to the array. (Notice that the order in which they happen does not matter)
- 25% of the time, noting happens to the array.

Moreover, there is no indication of what effect the quantum fluctuation has had
each time. The consortium is now concerned, and it has hired you to get its
percious data back, in whatever form it is in! Can you find the entire array, such
that your answer is accurate as of the time that you give it? Answering does not
count as a query, so if you answer after your 30th query, for example, the array
will be the same as it was after your 21st through 30th queries.


# https://github.com/theXYZT/codejam-2020/blob/master/Qualification%20Round/esab-atad.py

"""

# I/O Code
import sys


class Case:
    def __init__(self, nbits):
        self.nbits = nbits
        self.data = ['*'] * self.nbits
        self.complement_id = None
        self.reverse_id = None

    def query(self, i):
        print(str(i + 1), flush=True)
        response = input()
        if response == 'N':
            sys.exit()
        return response

    def query_pairs(self, i):
        # Reads i-th position from the beginning and from the end
        j = self.nbits - i - 1
        self.data[i] = self.query(i)
        self.data[j] = self.query(j)

        # Finds reference positions in data for configuration check
        if self.complement_id is None and self.data[i] == self.data[j]:
            self.complement_id = i
        if self.reverse_id is None and self.data[i] != self.data[j]:
            self.reverse_id = i

    def reverse(self):
        self.data = self.data[::-1]

    def complement(self):
        flip = {'0': '1', '1': '0'}
        self.data = [flip[c] if c in flip else c for c in self.data]

    def check_if_reversed(self):
        if self.reverse_id is None:
            _ = self.query(0)  # Waste a query
        else:
            if self.data[self.reverse_id] != self.query(self.reverse_id):
                self.reverse()

    def check_if_complemented(self):
        if self.complement_id is None:
            _ = self.query(0)  # Waste a query
        else:
            if self.data[self.complement_id] != self.query(self.complement_id):
                self.complement()

    def solve(self):
        read_position = 0

        # Read first 5 and last 5 positions
        for i in range(5):
            self.query_pairs(i)
            read_position += 1

        while '*' in self.data and read_position < self.nbits // 2:
            # Use two queries to check data configuration
            # Between every four paired queries
            if read_position % 4 == 1:
                self.check_if_complemented()
                self.check_if_reversed()

            self.query_pairs(read_position)
            read_position += 1

        print("".join(self.data), flush=True)
        if input() == 'N':
            sys.exit()


num_cases, num_bits = map(int, input().split())

for _ in range(1, num_cases + 1):
    case = Case(num_bits)
    case.solve()

sys.exit()

"""
Given a number n, find length of the longest consecutive 1s in its binary representation.

Examples :

Input : n = 14
Output : 3
The binary representation of 14 is 1110.

The idea is based on the concept that if we AND a bit sequence with a shifted version of itself, we’re effectively
removing the trailing 1 from every sequence of consecutive 1s.So the operation x = (x & (x << 1)) reduces length of
every sequence of 1s by one in binary representation of x. If we keep doing this operation in a loop, we end up with
x = 0. The number of iterations required to reach 0 is actually length of the longest consecutive sequence of 1s.
"""


def count_max_consecutive_1s(no):
    count = 0
    while no != 0:
        no = no & (no << 1)
        count += 1
    return count


print(count_max_consecutive_1s(14))

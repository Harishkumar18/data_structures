"""
A simple approach is to compute the factorial, and then count the number of trailing zeros by continuously
dividing by ten. The problem with this though is that the bounds of an int would be exceeded very
quickly. To avoid this issue, we can look at this problem mathematically.
Consider a factorial like 19 ! :
19! = 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19
A trailing zero is created with multiples of 10, and multiples of 10 are created with pairs of 5-multiples and
2-multiples.
Therefore, to count the number of zeros, we only need to count the pairs of multiples of 5 and 2. There will
always be more multiples of 2 than 5, though, so simply counting the number of multiples of 5 is sufficient.
"""


def factorial_five(num):
    count = 0
    while num % 5 == 0:
        count += 1
        num /= 5
    return count


def count_trail_zeros(num):
    count = 0
    for i in range(2, num + 1):
        count += factorial_five(i)
    return count


class Solution:
    """this approach is of O(log n) complexity"""
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        if A < 5:
            return 0
        for i in range(5, A + 1, 5):
            count += self.find_factors(i)
        return count

    def find_factors(self, no):
        count = 0
        while not no % 5:
            count += 1
            no = int(no / 5)
        return count

print(count_trail_zeros(20))

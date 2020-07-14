"""

"""


class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        if not A:
            return A
        res, cur, num_of_letters = [], [], 0
        for w in A:
            if num_of_letters + len(A) + len(cur) > B:
                for i in range(B - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                print(cur)
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [A]
            num_of_letters += len(A)
        return res + [' '.join(cur).ljust(B)]


print(Solution().fullJustify(["What", "must", "be", "shall", "be."], 16))

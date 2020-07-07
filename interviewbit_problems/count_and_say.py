"""

"""


class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if not A:
            return A
        if A == 1:
            return "1"
        if A == 2:
            return "11"
        s = "11"
        for i in range(3, A+1):
            # we are processing previous value in the current iteration so to run
            # more iteration we are adding one dummy character to string
            s += "$"
            n = len(s)
            count = 1
            res = ""
            for j in range(1, n):
                if s[j] != s[j - 1]:
                    res += str(count)
                    res += s[j - 1]
                    count = 1
                else:
                    count += 1
            s = res
        return s

print(Solution().countAndSay(5))
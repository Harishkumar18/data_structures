"""

"""


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        mappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        i = 0
        while i < len(A):
            s1 = mappings[A[i]]
            if i + 1 < len(A):
                s2 = mappings[A[i + 1]]
                if s1 >= s2:
                    result+=s1
                    i += 1
                else:
                    result-=s1
                    i += 1
            else:
                result += s1
                i += 1

        return result


print(Solution().romanToInt("IV"))
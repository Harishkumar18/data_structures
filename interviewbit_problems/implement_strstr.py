"""

"""


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        if not A or not B:
            return 0
        for i in range(len(A) - len(B)+1):
            if A[i:i+len(B)] == B:
                return i
        return -1


A = "welcome"
B = "come"
print(Solution().strStr(A, B))
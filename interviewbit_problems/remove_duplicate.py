"""

"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 1:
            return 0
        n = len(A)
        if n == 1:
            return 1
        i = 0
        j = 1
        while i < n and j < n:
            if A[j] == A[i]:
                j+=1
            else:
                A[i+1] = A[j]
                print(A[i+1])
                i+=1
                j+=1
        return A

A = [1,2,2]
print(Solution().removeDuplicates(A))
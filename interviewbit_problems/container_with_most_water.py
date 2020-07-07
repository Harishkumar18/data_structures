"""

"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        if len(A) <= 1:
            return 0
        left = 0
        right = len(A)-1
        max_value = -2**31
        while left < right:
            min_value = min(A[left], A[right])
            distance = right - left
            max_value = max(max_value, min_value*distance)
            if A[left] < A[right]:
                left+=1
            else:
                right-=1
        return max_value

A = [1,5,4,3]
print(Solution().maxArea(A))
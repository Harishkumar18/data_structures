"""
Description: rotate the array

"""
from typing import List
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k:]+nums[:n-k]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = deque(nums)
        d.rotate(k)
        nums[:] = list(d)


s1 = Solution()
inp_list = [1, 2, 3, 4, 5]
s1.rotate(inp_list, 1)
# s1.rotate2(inp_list, 6)
print(inp_list)

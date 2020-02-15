"""
Desc: get the index of getting two nums
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index, each in enumerate(nums):
            print(each)
            remaining = target - each
            print("rem", remaining)
            if remaining in nums and remaining!=each:
                result.append(index)
                result.append(nums.index(remaining))
                break
        return result


s1 = Solution()
nums = [3,2,4]
res = s1.twoSum(nums, 6)
print(res)

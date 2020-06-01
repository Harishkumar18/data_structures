class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for element in range(len(nums)):
            j = 0
            count = 0
            while j < len(nums):
                if nums[element] > nums[j]:
                    count += 1
                j += 1
            print("element and j", element)
            print(j)
            result.append(count)
        return result


print(Solution().smallerNumbersThanCurrent([7,7,7,7]))

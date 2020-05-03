"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


def find_tripplets(array, target):
    ans = []
    array.sort()
    for i in range(0, len(array)-2):
        for j in range(i + 1, len(array)-1):
            for k in range(len(array) - 1, 1, -1):
                print(i, j, k)
                if array[i] + array[j] + array[k] == target:
                    ans.append([array[i], array[j], array[k]])
                elif array[i] + array[j] + array[k] < target:
                    print("harish")
                    j += 1
                else:
                    k -= 1
    return ans


array = [-1, 0, 1, 2, -1, -4]
target = 0
result = find_tripplets(array, target)
print(result)

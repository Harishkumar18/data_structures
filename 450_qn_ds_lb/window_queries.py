"""
You are given two lists of integers nums and queries. You are also given an integer w. Return a new list where for each query q in queries, we answer the question of how many number of different ways are there for a window of length w to cover an element with value q.

Constraints

n ≤ 100,000 where n is the length of nums
m ≤ n where m is the length of queries
0 ≤ nums[i] < n
0 ≤ queries[i] < n
Example 1
Input

nums = [2, 1, 2, 3, 4]
queries = [2, 1]
w = 3
Output

[3, 2]
Explanation

For the first query, we ask how many ways are there for a window of length 3 to contain the value 2. There are three ways:

[2, 1, 2]
[1, 2, 3]
[2, 3, 4]
For the second query, we ask how many ways are there for a window of length 3 to contain the value 1. There are two ways:

[2, 1, 2]
[1, 2, 3]
Example 2
Input

nums = [2, 2, 2]
queries = [2]
w = 2
Output

[2]
https://binarysearch.com/problems/Window-Queries
"""

# brute force solution
# below code is failing due to time limit


class Solution:
    def solve(self, nums, queries, w):
        res = []
        for i in queries:
            count = 0
            for each in range(len(nums)-w+1):
                if i in nums[each:(each+w)]:
                    count+=1
            res.append(count)
        return res
        


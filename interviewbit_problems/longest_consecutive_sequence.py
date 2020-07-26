"""
"Longest consecutive sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity."
"""


class Solution:
    def longestConsecutive(self, arr):
        if not arr:
            return 0
        arr = set(arr)
        maxlen = 0
        for x in arr:
            if x - 1 not in arr:
                y = x + 1
                while y in arr:
                    y += 1
                maxlen = max(maxlen, y - x)
        return maxlen


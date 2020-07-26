"""
"Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] "

"""

from collections import deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, arr, k):
        if not arr:
            return arr
        d = deque()
        res = []
        for i in range(k):
            # make sure the deques contains decreasing sequence of elements
            while d and arr[d[-1]] < arr[i]:
                d.pop()
            d.append(i)
        for i in range(k, len(arr)):
            res.append(arr[d[0]])
            # make sure to remove the element not in current sliding window
            while d and d[0] <= i - k:
                d.popleft()

            # make sure the deque containse decresing sequence of elements
            while d and arr[d[-1]] < arr[i]:
                d.pop()
            d.append(i)
        # make sure to add the first element in deque bcoz we iterated till n
        res.append(arr[d[0]])

        return res
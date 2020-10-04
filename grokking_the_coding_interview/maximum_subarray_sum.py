"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""


def max_subarray_sum__brute_force_approach(inp_list, k):
    """
    TC: O(N*K) k operations for n elements
    """
    maxsum = 0
    n = len(inp_list)
    for i in range(n - k + 1):
        currsum = sum(inp_list[i:i + k])
        if currsum > maxsum:
            maxsum = currsum
    return maxsum


def max_subarray_sum(inp_list, k):
    """
    TC: O(N)
    SC: O(1)

    To calculate the sum of the next subarray, we need to slide the window ahead by one element. So to slide the
    window forward and calculate the sum of the new position of the sliding window, we need to do two things:
    Subtract the element going out of the sliding window i.e., subtract the first element of the window. Add the new
    element getting included in the sliding window i.e., the element coming right after the end of the window.
    """
    max_sum, window_sum = 0, 0
    window_start = 0
    for i in range(len(inp_list)):
        window_sum += inp_list[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= inp_list[window_start]
            window_start += 1
    return max_sum


k = 3
print(max_subarray_sum([2, 1, 5, 1, 3, 2], k))
print(max_subarray_sum([2, 3, 4, 1, 5], 2))

"""
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
the ith histogram’s bar. Width of each bar is 1.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Find the area of largest rectangle in the histogram.

Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
Explanation 1:
    The largest rectangle is shown in the shaded area, which has area = 10 unit.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, heights):
        stack = [-1]
        maxarea = 0
        for i in range(len(heights)):
            while stack[-1]!=-1 and heights[stack[-1]] >= heights[i]:
                lastelementindex = stack.pop()
                maxarea = max(maxarea, heights[lastelementindex] * (i-stack[-1]-1))
            stack.append(i)
        while stack[-1]!=-1:
            index_elem = stack.pop()
            maxarea = max(maxarea, heights[index_elem]*(len(heights)-stack[-1]-1))
        return maxarea

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
"""


def maximalrectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n+1)
    ans = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i]+1 if row[i] == "1" else 0
        print(height)
        stack = [-1]
        for i in range(n+1):
            while height[i] < height[stack[-1]]:
                print(height)
                h = height[stack.pop()]
                print(h)



matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
res = maximalrectangle(matrix)
# print(res)
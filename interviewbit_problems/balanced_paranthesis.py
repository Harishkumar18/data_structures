"""
Problem Description

Given a string A consisting only of '(' and ')'.

You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if not A:
            return A
        stack = []
        for i in A:
            if i == "(":
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                return 0
        if not stack:
            return 1
        return 0

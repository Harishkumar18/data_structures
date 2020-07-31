"""
Problem Description

Given a Binary Tree A containing N nodes.

You need to find the path from Root to a given node B.

NOTE:
No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.

Problem Constraints
1 <= N <= 105

1 <= Data Values of Each Node <= N

1 <= B <= N

Input Format
First Argument represents pointer to the root of binary tree A.

Second Argument is an integer B denoting the node number.

Output Format
Return an one-dimensional array denoting the path from Root to the node B in order.
"""


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root, target):
        self.res = []
        if not root:
            return self.res
        self.dfs(root, target, [])
        return self.res
        
    def dfs(self, root, target, ls):
        if not root:
            return
        if root.val == target:
            ls = ls+[root.val]
            self.res = ls[:]
            return self.res
        self.dfs(root.left, target, ls+[root.val])
        self.dfs(root.right, target, ls+[root.val])

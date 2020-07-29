"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
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
    # @return a list of list of integers
    def pathSum(self, root, total):
        if not root:
            return root
        res = []
        self.dfs(root, total, [], res)
        return res
    
    def dfs(self, root, total, ls, res):
        if not root:
            return
        if root.val ==total and not(root.left or root.right):
            ls = ls+[root.val]
            res.append(ls)
        self.dfs(root.left, total-root.val, ls+[root.val], res)
        self.dfs(root.right, total-root.val, ls+[root.val], res)
            

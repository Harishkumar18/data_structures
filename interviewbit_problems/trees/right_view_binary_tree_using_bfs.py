"""
Problem Description

Given a binary tree A of integers. Return an array of integers representing the right view of the Binary tree.

Right view of a Binary Tree: is a set of nodes visible when the tree is visited from Right side.

TC: O(n)
SC: O(n) where the tree is the tree is right skewed binary tree
"""


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        res = []
        if not root:
            return root
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                curr_elem = queue.pop(0)
                if(i==n-1):
                    res.append(curr_elem.val)
                if curr_elem.left:
                    queue.append(curr_elem.left)
                if curr_elem.right:
                    queue.append(curr_elem.right)
        return res
            

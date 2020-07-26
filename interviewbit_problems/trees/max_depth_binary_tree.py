"""
"Max Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node."
"""


# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        lefttree = 1+ self.maxDepth(root.left)
        righttree = 1+ self.maxDepth(root.right)
        return max(lefttree, righttree)

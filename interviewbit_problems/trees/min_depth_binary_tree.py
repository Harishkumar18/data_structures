"""
"Min Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node."
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
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + (self.minDepth(root.right))
        if not root.right:
            return 1 + (self.minDepth(root.left))
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


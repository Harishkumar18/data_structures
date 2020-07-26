"""
Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes’ values.

Using recursion is not allowed.
"""


# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return root
        stack, res = [], []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res



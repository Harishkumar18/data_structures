"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            curr = root.left
            while curr.right:
                curr = curr.right
            curr.right = root.right
            root.right = root.left
            root.left = None
        return root


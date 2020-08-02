"""
Least common ancestor

Find the lowest common ancestor in an unordered binary tree given two values in the tree.
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        # update ca field
        self.count = 0
        result = self.lca2(A, B, C)
        return result.val if (result and self.count == 2) else -1

    def lca2(self, root, p, q):
        if not root:
            return root
        left = self.lca2(root.left, p, q)
        right = self.lca2(root.right, p, q)
        if root.val == p or root.val == q:
            self.count += 1
            if root.val == p and root.val == q:
                self.count += 1
            return root
        if left and right:
            return root
        if not left and not right:
            return
        return left if left else right


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, root, total):
        if not root:
            return 0
        if not root.left and not root.right and root.val == total:
            return 1
        return self.hasPathSum(root.left, total-root.val) or self.hasPathSum(root.right, total-root.val)

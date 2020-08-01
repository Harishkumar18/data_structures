"""
Construct Binary Tree From Inorder And Preorder
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        if inorder:
            node_index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[node_index])
            root.left = self.buildTree(preorder, inorder[0:node_index])
            root.right = self.buildTree(preorder, inorder[node_index+1:])
            return root

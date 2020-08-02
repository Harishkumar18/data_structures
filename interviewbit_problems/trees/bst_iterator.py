"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.addnodes(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack != []

    # @return an integer, the next smallest number
    def next(self):
        root = self.stack.pop()
        self.addnodes(root.right)
        return root.val

    def addnodes(self, root):
        while root:
            self.stack.append(root)
            root = root.left

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

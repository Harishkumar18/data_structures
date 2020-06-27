"""
check balanced tree with reduced complexity compared to previous one
This code runs in O(N) time and O(H) space, where H is the height of the tree.
"""

import sys


# node in the binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isbalanced(root, height):
    if root is None:
        return True
    lh = Height()
    rh = Height()
    left_tree = isbalanced(root.left, lh)
    right_tree = isbalanced(root.right, rh)
    height.height = max(lh.height, rh.height)+1
    print("left tree", left_tree)
    print("right tree", right_tree)
    if abs(lh.height-rh.height)<=1:
        return left_tree and right_tree
    return False


height = Height()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.left.left.left = Node(9)
# root.right.left.right = Node(6)
print(isbalanced(root, height))
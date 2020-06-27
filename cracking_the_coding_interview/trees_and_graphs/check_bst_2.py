"""
1) Do In-Order Traversal of the given tree and store the result in a temp array.
3) Check if the temp array is sorted in ascending order, if it is, then the tree is BST.

Time Complexity: O(n)

We can avoid the use of Auxiliary Array. While doing In-Order traversal, we can keep track of previously visited node. If the value of the currently visited node is less than the previous value, then tree is not BST. Thanks to ygos for this space optimization.
filter_none
"""
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isbst(root):
    prev = None
    return isbstutil(root, prev)


def isbstutil(root, prev):
    if root is None:
        return True
    if isbstutil(root.left, prev) is False:
        return False
    if prev is not None:
        if prev.data>root.data:
            return False
    prev = root
    return isbstutil(root.right, prev)


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(3)
root.right.right = Node(6)
print(isbst(root))
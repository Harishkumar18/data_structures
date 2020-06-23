"""
to find the maximum height of the binary tree
"""


# node in the binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maximum_height(root):
    if root is None:
        return 0
    return max(1+maximum_height(root.left), 1+maximum_height(root.right))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(maximum_height(root))
"""
to check the tree is balanced or not
not an efficient solution
TS: O(n log n)
because we are checking the height in all nodes
"""


# node in the binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_height(root):
    if root is None:
        return 0
    return max(1+get_height(root.left), 1+get_height(root.right))


def isbalanced(root):
    if root is None:
        return 0
    height_diff = abs(get_height(root.left)-get_height(root.right))
    if height_diff >1:
        return False
    else:
        if isbalanced(root.left) and isbalanced(root.right):
            return True
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
# root.right.left.right = Node(6)
print(isbalanced(root))
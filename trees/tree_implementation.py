# node in the binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def infix_expression(root):
    """function which will iterate through the tree to find the infix expression"""
    if root is None:
        return None
    infix_expression(root.left)
    print(root.val)
    infix_expression(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
infix_expression(root)
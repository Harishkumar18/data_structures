"""
Given a binary search tree and a number, inserts a  new node with the given number in the correct place
in the tree. Returns the new root pointer which the caller should then use( the standard trick to avoid
using reference parameters).

Complexity Analysis:

Time Complexity: O(h), where h is the height of the tree.
As in the second case(suppose skewed tree) we have to travel all the way towards the root.
Auxiliary Space: O(1).
Due to no use of any data structure for storing values.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.val:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node


def minimum_value(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current


def inordersuccessor(root, target):
    if root is None:
        return None
    if target.right is not None:
        return minimum_value(target.right)

    parent_node = target.parent
    while parent_node and target:
        if parent_node.left == target:
            return parent_node
        target = parent_node
        parent_node = parent_node.parent


def print_tree(root):
    if root is None:
        return None
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)


root = None
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)
# print_tree(root)
temp = root.left.right.right.parent
print(root.left.parent.val)
# temp = root.left
# print(inordersuccessor(root, temp).val)
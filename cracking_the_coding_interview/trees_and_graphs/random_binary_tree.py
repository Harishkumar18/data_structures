from random import randint


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.children = 0


def getElements(root):
    if not root:
        return 0
    return getElements(root.left)+getElements(root.right)+1


def insertChildrenCount(root):
    if not root:
        return 0
    root.children = getElements(root) - 1
    insertChildrenCount(root.left)
    insertChildrenCount(root.right)


def children(root):
    if not root:
        return 0
    return root.children+1


def randomUtil(root, count):
    if not root:
        return 0
    if count == children(root.left):
        return root.val
    if count < children(root.left):
        return randomUtil(root.left, count)
    return randomUtil(root.right, count - children(root.left) - 1)


def randomNode(root):
    count = randint(0, root.children)
    return randomUtil(root, count)


def print_tree(root):
    if root is None:
        return None
    print_tree(root.left)
    print(f"root value is {root.val} and its children count {root.children}")
    print_tree(root.right)


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)
insertChildrenCount(root)
# print_tree(root)
res  = randomNode(root)
print(f"random node:{res}")
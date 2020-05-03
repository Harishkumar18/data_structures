# create-a-mirror-tree-from-the-given-binary-tree


class Node:
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None


def createNode(val):
    newnode = Node(0)
    newnode.val = val
    newnode.left = None
    newnode.right = None
    return newnode


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


def mirrorify(root, mirror):
    if root is None:
        mirror = None
        return mirror
    mirror = createNode(root.val)
    mirror.left = mirrorify(root.right, mirror.left)
    mirror.right = mirrorify(root.left, mirror.right)
    return mirror


if __name__ == '__main__':
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(6)
    tree.left.left = createNode(2)
    tree.left.right = createNode(4)
    print("original tree")
    inorder(tree)
    mirror = None
    mirror = mirrorify(tree, mirror)
    print("mirror tree")
    inorder(mirror)
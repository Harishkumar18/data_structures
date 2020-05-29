class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(inOrder, instart, inend, value):
    for element in range(instart, inend + 1):
        if inOrder[element] == value:
            return element


def build_tree(inOrder, preOrder, instart, inend):
    if instart > inend:
        return None

    tnode = Node(preOrder[build_tree.preindex])
    build_tree.preindex += 1

    if instart == inend:
        return tnode
    search_index = search(inOrder, instart, inend, tnode.data)
    tnode.left = build_tree(inOrder, preOrder, instart, search_index - 1)
    tnode.right = build_tree(inOrder, preOrder, search_index + 1, inend)
    return tnode


def inordertree(root):
    if root is None:
        return None
    inordertree(root.left)
    print(root.data)
    inordertree(root.right)


# Driver program to test above function
inOrder = [8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7]
preOrder = [1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7]
build_tree.preindex = 0
root = build_tree(inOrder, preOrder, 0, len(inOrder) - 1)
inordertree(root)

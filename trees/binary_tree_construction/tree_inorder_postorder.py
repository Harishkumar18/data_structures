# TODO: Need to modify


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(inOrder, instart, inend, value):
    # for element in range(instart, inend + 1):
    for element in range(len(inOrder)):
        if inOrder[element] == value:
            return element


def build_tree(inOrder, postOrder, instart, inend):
    if instart > inend:
        return None
    tnode = Node(postOrder[build_tree.postindex])
    build_tree.postindex -= 1

    if instart == inend:
        return tnode
    search_index = search(inOrder, instart, inend, tnode.data)
    tnode.left = build_tree(inOrder, postOrder, instart, search_index - 1)
    tnode.right = build_tree(inOrder, postOrder, search_index + 1, inend)
    return tnode


def inordertree(root):
    if root is None:
        return None
    inordertree(root.left)
    print(root.data)
    inordertree(root.right)


# Driver program to test above function
inOrder = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]
postOrder = [9, 1, 2, 12, 7, 5, 3, 11, 4, 8]
build_tree.postindex = 9
root = build_tree(inOrder, postOrder, 0, len(inOrder) - 1)
inordertree(root)

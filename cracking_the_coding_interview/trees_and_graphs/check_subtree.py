"""
Traverse the tree T in preorder fashion. For every visited node in the traversal, see if the subtree rooted with this node is identical to S.
Time worst case complexity of above solution is O(mn) where m and n are number of nodes in given two trees.
"""


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def areIdentical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 and not root2:
        return False
    return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)


def isSubtree(T, S):
    if not S:
        return True
    if not T:
        return False
    if areIdentical(T, S):
        return True
    return isSubtree(T.left, S) or isSubtree(T.right, S)

T = Node(26)
T.right = Node(3)
T.right.right  = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)

S = Node(10)
S.right = Node(6)
S.left = Node(4)
# S.left.right = Node(30)

if isSubtree(T, S):
    print("Tree 2 is subtree of Tree 1")
else:
    print("Tree 2 is not a subtree of Tree 1")
"""
Note that the previous method assumes that keys are present in Binary Tree. If one key is present and other is absent,
then it returns the present key as LCA (Ideally should have returned NULL).
We can extend this method to handle all cases by passing two boolean variables v1 and v2. v1 is set as true when n1
is present in tree and v2 is set as true if n2 is present in tree.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_lca_util(root, node1, node2, visited):
    if not root:
        return None
    if root.val == node1:
        visited[0] = True
        return root
    if root.val == node2:
        visited[1] = True
        return root
    left_st = find_lca_util(root.left, node1, node2, visited)
    right_st = find_lca_util(root.right, node1, node2, visited)
    if left_st and right_st:
        return root
    if not left_st and not right_st:
        return None
    return left_st if left_st is not None else right_st

def find(root, key):
    if not root:
        return None
    if root.val == key or find(root.left, key) or find(root.right, key):
        return True
    return None

def findLCA(root, node1, node2):
    if root is None:
        return None
    visited = [False, False]
    lca = find_lca_util(root, node1, node2, visited)
    if visited[0] and visited[1] or visited[0] and find(lca, node2) or visited[1] and find(lca, node1):
        return lca
    return None


root = Node(4)
root.left = Node(6)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(11)
root.left.right.left = Node(7)
res = findLCA(root, 6, 8)
if res:
    print(res.val)
else:
    raise Exception("Getting None value")
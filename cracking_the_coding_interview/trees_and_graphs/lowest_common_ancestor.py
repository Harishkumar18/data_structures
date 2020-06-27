"""
If any of the given keys (n1 and n2) matches with root, then root is LCA (assuming that both keys are present).
If root doesn’t match with any of the keys, we recur for left and right subtree. The node which has one key present
in its left subtree and the other key present in right subtree is the LCA. If both keys lie in left subtree, then left
subtree has LCA also, otherwise LCA lies in right subtree.

Time complexity of the above solution is O(n) as the method does a simple tree traversal in bottom up fashion.
Note that the above method assumes that keys are present in Binary Tree. If one key is present and other is absent,
then it returns the present key as LCA (Ideally should have returned NULL).
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_lowest_common_ancestor(root, node1, node2):
    if not root:
        return None
    if root.val == node1 or root.val == node2:
        return root
    left_st = find_lowest_common_ancestor(root.left, node1, node2)
    right_st = find_lowest_common_ancestor(root.right, node1, node2)
    if left_st and right_st:
        return root
    if not left_st and not right_st:
        return None
    return left_st if left_st is not None else right_st


root = Node(4)
root.left = Node(6)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(11)
root.left.right.left = Node(7)
res = find_lowest_common_ancestor(root, 2, 10)
if res:
    print(res.val)
else:
    raise Exception("Getting None value")
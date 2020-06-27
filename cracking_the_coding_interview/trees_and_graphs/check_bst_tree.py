"""
min/max solution
left. data<=current.data<right.data
We start with a range of (min = NULL, max = NULL), which the root obviously meets. (NULL indicates
that there is no min or max.) We then branch left, checking that these nodes are within the range ( min =
NULL, max = 20). Then, we branch right, checking that the nodes are within the range ( min = 20,
max = NULL).We proceed through the tree with this approach. When we branch left, the max gets updated. When we
branch right, the min gets updated. If anything fails these checks, we stop and return false.

Time Complexity: O(n)
Auxiliary Space : O(1) if Function Call Stack size is not considered, otherwise O(n)
"""
import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isbst(root):
    min_infi = -sys.maxsize-1
    max_infi = sys.maxsize
    return isbstutil(root, min_infi, max_infi)


def isbstutil(root, min_ele, max_ele):
    if root is None:
        return True
    if root.val < min_ele or root.val >= max_ele:
        return False
    return isbstutil(root.left, min_ele, root.val+1) and isbstutil(root.right, root.val+1, max_ele)


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
# root.right.left = Node(3)
# root.right.right = Node(6)
print(isbst(root))

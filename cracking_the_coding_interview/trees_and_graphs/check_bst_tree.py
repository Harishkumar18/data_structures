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















height = Height()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.left.left.left = Node(9)
# root.right.left.right = Node(6)
print(isbalanced(root, height))

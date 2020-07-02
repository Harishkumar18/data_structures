"""
Given a stream of integers, lookup the rank of a given integer x. Rank of an integer in stream is “Total number of
elements less than or equal to x (not including x)”.

If element is not found in stream or is smallest in stream, return -1.
Examples:

Input :  arr[] = {10, 20, 15, 3, 4, 4, 1}
              x = 4;
Output : Rank of 4 in stream is: 3
There are total three elements less than
or equal to x (and not including x)

We traverse the tree from root and compare the root values to x.
If root->data == x, return size of left subtree of root.
If x < root->data, return getRank(root->left)
If x > root->data, return getRank(root->right) + size of letSubtree + 1.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        # left sub tree count
        self.leftstcount = 0


def insert(root, elem):
    if root is None:
        return Node(elem)

    if elem < root.val:
        root.left = insert(root.left, elem)
        root.leftstcount += 1
    else:
        root.right = insert(root.right, elem)
    return root


def getRank(root, target):
    if not root:
        return -1
    if root.val == target:
        return root.leftstcount
    else:
        if root.val < target:
            if not root.right:
                return -1
            else:
                leftcount = getRank(root.right, target)
                if leftcount != -1:
                    return root.leftstcount + leftcount + 1
                else:
                    return -1
        else:
            if not root.left:
                return -1
            else:
                return getRank(root.left, target)


def printtree(root):
    if not root:
        return None
    printtree(root.left)
    print(f"tree node val is {root.val} and its left subtree height: {root.leftstcount}")
    printtree(root.right)


# arr = [5, 1, 4, 4, 5, 9, 7, 13, 3]
arr = [20, 15, 10, 5, 13, 25, 23, 24]
n = len(arr)
x = 25

root = None
for i in range(n):
    root = insert(root, arr[i])
print(getRank(root, 30))

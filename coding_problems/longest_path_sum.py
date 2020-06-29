"""
Vmware interview question find the longest path sum in binary tree
"""
import sys


# node in the binary tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_longest_path_sum(root, curr_sum, curr_len, MAXLEN, MAXSUM):
    if not root:
        if MAXLEN[0]<curr_len:
            MAXLEN[0] = curr_len
            MAXSUM[0] = curr_sum
        elif MAXLEN[0] == curr_len and MAXSUM[0]<curr_sum:
            MAXSUM[0] = curr_sum
        return
    get_longest_path_sum(root.left, curr_sum+root.val, curr_len+1, MAXLEN, MAXSUM)
    get_longest_path_sum(root.left, curr_sum + root.val, curr_len + 1, MAXLEN, MAXSUM)
    return MAXSUM[0]


def find_longest_path_sum(root):
    if not root:
        return 0
    MAXSUM = [-sys.maxsize-1]
    MAXLEN = [0]
    curr_sum = 0
    curr_len = 0
    return get_longest_path_sum(root, curr_sum, curr_len, MAXLEN, MAXSUM)





root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(1)
root.left.right.left = Node(6)
root.right.left = Node(2)
root.right.right = Node(3)
print(find_longest_path_sum(root))






"""
You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class CountTarget:
    def count_target_sum(self, root, target):
        if not root:
            return None
        self.no_of_paths = 0
        self.dfs(root, target)
        return self.no_of_paths

    def dfs(self, root, target):
        if not root:
            return
        self.process_tree(root, target)
        self.dfs(root.left, target)
        self.dfs(root.right, target)

    def process_tree(self, root, target):
        if not root:
            return
        if target == root.val:
            self.no_of_paths+=1
        self.process_tree(root.left, target-root.val)
        self.process_tree(root.right, target-root.val)


root = Node(10)
root.left = Node(-1)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.left = Node(16)
root.right.right = Node(1)
no_of_paths = CountTarget().count_target_sum(root, 160)
print(no_of_paths)
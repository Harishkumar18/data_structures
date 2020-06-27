from itertools import zip_longest

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leafSimilar(root1, root2):
    def dfs(n):
        if not n:
            return
        if not n.left and not n.right:
            yield n.val
        yield from dfs(n.left)
        yield from dfs(n.right)
    return all(a == b for a, b in zip_longest(dfs(root1), dfs(root2)))


root = Node(5)
root.left  = Node(6)
root.right = Node(7)
root.left.right  = Node(1)
root.left.left = Node(2)
root1 = Node(15)
root1.left  = Node(16)
root1.right = Node(7)
root1.left.right  = Node(1)
root1.left.left = Node(2)
res = leafSimilar(root, root1)
print(res)
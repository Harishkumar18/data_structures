"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traverse(self, func, level=0):
        if self.left:
            self.left.traverse(func, level+1)
        func(self, level)
        if self.right:
            self.right.traverse(func, level+1)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(7)
root.left.right = TreeNode(1)
root.right.left = TreeNode(2)
root.right.right = TreeNode(3)


#approach1
d = {}
def fillDict(node, level):
    if level in d:
        l = d[level]
        l.append(node)
    else:
        d[level] = [node]
root.traverse(fillDict)
print(d)

# approach 2
def createListsFromTree2(treeNode):
    d = {}
    def fillDict(node, level):
        d.setdefault(level, []).append(node)
    treeNode.traverse(fillDict)
    return  d

#approach3
from collections import defaultdict
def createListsFromTree3(treeNode):
    d = defaultdict(list)
    def fillDict(node, level):
        d[level].append(node)
    treeNode.traverse(fillDict)
    return  d
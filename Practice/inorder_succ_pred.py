"""
Qn: Inorder predecessor and successor for a given data in BST

Approach:
Input: root node, key
output: predecessor node, successor node

1. If root is NULL
      then return
2. if key is found then
    a. If its left subtree is not null
        Then predecessor will be the right most 
        child of left subtree or left child itself.
    b. If its right subtree is not null
        The successor will be the left most child 
        of right subtree or right child itself.
    return
3. If key is smaller then root node
        set the successor as root
        search recursively into left subtree
    else
        set the predecessor as root
        search recursively into right subtree
"""


class Node:
    # constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right=None


# function which will find the predecessor and successor
def find_predecessor_successor(root, key):
    # base case
    if not root:
        return

    # if data is present in the root
    if root.data == key:
        # maximum value in left subtree is a predecessor
        if root.left is not None:
            temp = root.left
            while(temp.right):
                temp = temp.right
            find_predecessor_successor.pre = temp

        # minimum value in right subtree is a successor
        if root.right is not None:
            temp=root.right
            while(temp.left):
                temp=temp.left
            find_predecessor_successor.succ = temp

    # if key is smaller than current node
    if root.data > key:
        find_predecessor_successor.succ = root
        # print("succ goes", find_predecessor_successor.succ.data)
        find_predecessor_successor(root.left, key)
    # if key is greater than current node
    # else:
    if root.data < key:
        find_predecessor_successor.pre = root
        find_predecessor_successor(root.right, key)


# utility function to add new nodes in BST
def insert(node, data):
    if node is None:
        return Node(data)

    if node.data < data:
        node.right = insert(node.right, data)
    else:
        node.left = insert(node.left, data)
    return node


# print inorder traversal from the tree
def printInordertraversal(root):
    if root:
        printInordertraversal(root.left)
        print(root.data)
        printInordertraversal(root.right)


root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

# inorder traversal for the tree
# print(printInordertraversal(root))
# static variables of the function find_predecessor_successor
find_predecessor_successor.pre = None
find_predecessor_successor.succ = None

find_predecessor_successor(root, key=60)

if find_predecessor_successor.pre is not None:
    print(f"predecessor is {find_predecessor_successor.pre.data}")
else:
    print(f"no predecessor")

if find_predecessor_successor.succ is not None:
    print(f"successor is {find_predecessor_successor.succ.data}")
else:
    print(f"no successor")




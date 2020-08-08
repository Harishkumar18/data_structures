class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class solution:
    def LCA(self, root, p, q):
        if not root:
            return root
        self.found = 0
        result = self.find_lca(root, p, q)
        return result.val if (result and self.found==2) else None

    def find_lca(self, root, p, q):
        if not root:
            return
        left = self.find_lca(root.left, p, q)
        right = self.find_lca(root.right, p, q)
        # print("left", left.val)
        # print("right", right.val)
        if root.val == p or root.val == q:
            self.found+=1
            if root.val==p and root.val==q:
                self.found+=1
            return root
        if left and right:
            return root
        if not left and not right:
            return None
        return left if left else right


#[3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
soln = solution()
res = soln.LCA(root, 5, 4)
print(res)

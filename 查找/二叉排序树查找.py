class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, node):
        if not root or root.val == node.val:
            return root
        if root.val > node.val:
            return self.searchBST(root.left, node)
        else:
            return self.searchBST(root.right, node)


root = BiTree(45)
a = BiTree(12)
b = BiTree(53)
root.left = a
root.right = b
a.left = BiTree(3)
a.right = BiTree(37)
a.right.left = BiTree(24)
b.right = BiTree(100)
b.right.left = BiTree(61)
b.right.left.right = BiTree(90)
b.right.left.right.left = BiTree(78)
node = BiTree(70)

res = Solution().searchBST(root, node)
if res:
    print(res.val)
else:
    print(res)

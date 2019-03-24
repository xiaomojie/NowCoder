# 其实就是前序遍历
class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def deep_traversal(self, root):
        # 迭代法
        res = []
        if not root:
            return res

        stack = [root]
        while len(stack):
            p = stack.pop()
            res.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return res

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
print(Solution().deep_traversal(root))
# [45, 12, 3, 37, 24, 53, 100, 61, 90, 78]

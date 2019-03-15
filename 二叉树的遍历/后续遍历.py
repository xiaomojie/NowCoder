class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionRecursion:
    def postorder_traversal(self, root):
        if not root:
            return []
        return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.val]


class SolutionCirculation:
    def postorder_traversal(self, root):
    # 左右中，其逆序为中右左，先求中右左在求数组的逆序
        res = []
        if not root:
            return res
        stack = []
        p = root
        while p or len(stack):
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.right
            else:
                p = stack.pop().left
        return res[::-1]
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
print(SolutionRecursion().postorder_traversal(root))
print(SolutionCirculation().postorder_traversal(root))
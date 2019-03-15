class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归法
class SolutionRecursion:
    # def preorder(self, root):
    #     res = []
    #     if not root:
    #         return res
    #     self.traversal(root, res)
    #     return res
    #
    # def traversal(self, root, res):
    #     if not root:
    #         return
    #     res.append(root.val)
    #     self.traversal(root.left, res)
    #     self.traversal(root.right, res)

    def preorder_traversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorder_traversal(root.left) + self.preorder_traversal(root.right)


class SolutionCirculation:
    def preorder_traversal(self, root):
        res = []
        if not root:
            return res
        stack = []
        p = root
        while p or len(stack):
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop().right
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
print(SolutionRecursion().preorder_traversal(root))
# print(SolutionRecursion().preorder(root))
print(SolutionCirculation().preorder_traversal(root))

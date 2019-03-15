class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionRecursion:
    # def inorder(self, root):
    #     res = []
    #     if not root:
    #         return res
    #     self.traversal(root, res)
    #     return res
    #
    # def traversal(self, root, res):
    #     if not root:
    #         return
    #     self.traversal(root.left, res)
    #     res.append(root.val)
    #     self.traversal(root.right, res)

    def inorder_traversal(self, root):
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

class SolutionCirculation:
    def inorder_traversal(self, root):
        res = []
        if not root:
            return res
        stack = []
        p = root
        while p or len(stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right
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
print(SolutionRecursion().inorder_traversal(root))
# print(SolutionRecursion().inorder(root))
print(SolutionCirculation().inorder_traversal(root))
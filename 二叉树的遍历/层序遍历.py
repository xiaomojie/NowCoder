class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solutionCirculation:
    def level_order_traversal(self, root):
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            p = queue.pop(0)
            res.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        return res

class solutionRecursion:
    def level_order_traversal(self, root):
        if not root:
            return []
        res = [[]]
        self.recursion(root, 1, res)
        return [k for item in res[:-1] for k in item]
    def recursion(self, root, level, res):
        if not root:
            return
        else:
            res[level - 1].append(root.val)
            if len(res) == level:
                res.append([])
            self.recursion(root.left, level + 1, res)
            self.recursion(root.right, level + 1, res)


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
print(solutionCirculation().level_order_traversal(root))
print(solutionRecursion().level_order_traversal(root))



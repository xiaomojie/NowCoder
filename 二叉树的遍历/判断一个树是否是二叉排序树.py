class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = True
        self.last = float('-inf')
    def isBSTree(self, root):
        if root.left and self.flag:
            self.isBSTree(root.left)
        if root.val < self.last:
            self.flag = False
        self.last = root.val
        if root.right and self.flag:
            self.isBSTree(root.right)
        return self.flag
    
a = BiTree(12)
b = BiTree(5)
c = BiTree(18)
d = BiTree(2)
e = BiTree(9)
f = BiTree(15)
g = BiTree(19)
h = BiTree(13)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
f.left = h
m = Solution().isBSTree(a)
print(m)





"""
给定一颗二叉搜索树（不是二叉平衡树），删除其中一个给定的节点
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 递归法
    def deleteNodeRecursion(self, root, key):
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNodeRecursion(root.left, key)
        elif root.val < key:
            root.right = self.deleteNodeRecursion(root.right, key)
        else:
            if not root.left or not root.right:
                root = root.left if root.left else root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNodeRecursion(root.right, cur.val)
        return root

    def traversal(self, root):
        if not root:
            return []
        return [root.val] + self.traversal(root.left) + self.traversal(root.right)

root = TreeNode(45)
a = TreeNode(12)
b = TreeNode(53)
root.left = a
root.right = b
a.left = TreeNode(3)
a.right = TreeNode(37)
a.right.left = TreeNode(24)
b.right = TreeNode(100)
b.right.left = TreeNode(61)
b.right.left.right = TreeNode(90)
b.right.left.right.left = TreeNode(78)
s = Solution()
print(s.traversal(root))
# t1 = s.deleteNodeRecursion(root, 45)
# print(s.traversal(t1))
# t1 = s.deleteNodeRecursion(root, 53)
# t1 = s.deleteNodeRecursion(root, 100)
t1 = s.deleteNodeRecursion(root, 12)
print(s.traversal(t1))
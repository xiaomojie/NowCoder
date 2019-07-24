class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

class Solution:
    def inorder_traversal(self, root):
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

    def KthNode(self, pRoot, k):
        if not pRoot:
            return None
        nums = self.inorder_traversal(pRoot)
        return nums[k-1]


root = TreeNode(5)
a = TreeNode(3)
b = TreeNode(7)
root.left = a
root.right = b
a.left = TreeNode(2)
a.right = TreeNode(4)
b.left = TreeNode(6)
b.right = TreeNode(8)

print(Solution().KthNode(root, 3))
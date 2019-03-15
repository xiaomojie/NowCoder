class BiTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, node, parent):
        if not root:
            return False, parent
        if root.val == node:
            return True, None
        elif root.val > node:
            return self.searchBST(root.left, node, root)
        else:
            return self.searchBST(root.right, node, root)

    def insertBST(self, root, node):
        parent = None
        flag, parent = self.searchBST(root, node, parent)
        if not flag:
            if not parent:
                root = BiTree(node)
            elif root.val > node:
                parent.left = BiTree(node)
            else:
                parent.right = BiTree(node)
        return root

root = None
root = Solution().insertBST(root, 45)
root = Solution().insertBST(root, 24)
root = Solution().insertBST(root, 53)
root = Solution().insertBST(root, 12)
root = Solution().insertBST(root, 90)
print(root.val, root.left.val, root.right.val, root.left.left.val, root.right.right.val)

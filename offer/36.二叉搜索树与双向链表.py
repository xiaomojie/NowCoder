# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        head = cur = TreeNode(0)
        self.ConvertTreeToList(pRootOfTree, cur)
        head = head.right
        head.left = None
        return head

    def ConvertTreeToList(self, root, cur):

        if root.left:
            cur = self.ConvertTreeToList(root.left, cur)
        cur.right = root
        root.left = cur
        cur = root
        if root.right:
            cur = self.ConvertTreeToList(root.right, cur)
        return cur


# {10,6,14,4,8,12,16}

root = TreeNode(10)
left1 = TreeNode(6)
right1 = TreeNode(14)
root.left = left1
root.right = right1

left2 = TreeNode(4)
right2 = TreeNode(8)
left1.left = left2
left1.right = right2

right1.left = TreeNode(12)
right1.right = TreeNode(16)
# cur = root
# while cur:
#     print(cur.val)
#     cur = cur.right

head = Solution().Convert(root)
cur = head
# print(head)
while cur.right:
    print(cur.val)
    cur = cur.right

print()
while cur:
    print(cur.val)
    cur = cur.left

# 调试的时候10的right还是14的left不对
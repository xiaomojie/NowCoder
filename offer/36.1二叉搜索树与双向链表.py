'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert1(self, pRootOfTree):
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

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        head = cur = TreeNode(0)
        stack = []
        p = pRootOfTree
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                cur.right = p
                p.left = cur
                cur = cur.right
                p = p.right

        head = head.right
        head.left = None
        return head


root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
print(Solution().Convert(root).val)




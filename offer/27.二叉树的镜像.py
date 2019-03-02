# -*- coding:utf-8 -*-
"""
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        if not root.left and not root.right:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.Mirror(root.left)
        self.Mirror(root.right)


# -*- coding:utf-8 -*-
"""
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，
定义其为对称的。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # 判断是否是对称的二叉树，可以自定义一种遍历方式，中右左，前序遍历对称的遍历算法
        # 若两种遍历方式得到的序列一样，则该二叉树是对称的二叉树

        return self.isSymmetricalRecursion(pRoot, pRoot)

    def isSymmetricalRecursion(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetricalRecursion(pRoot1.left, pRoot2.right) and \
               self.isSymmetricalRecursion(pRoot1.right, pRoot2.left)

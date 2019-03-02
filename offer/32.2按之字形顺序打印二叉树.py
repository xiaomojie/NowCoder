# -*- coding:utf-8 -*-
"""
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        odd_stack = [pRoot]
        even_stack = []
        res = []
        row = []
        while odd_stack or even_stack:
            if odd_stack:
                while odd_stack:
                    node = odd_stack.pop()
                    row.append(node.val)
                    if node.left:
                        even_stack.append(node.left)
                    if node.right:
                        even_stack.append(node.right)
                res.append(row)
                row = []
            else:
                while even_stack:
                    node = even_stack.pop()
                    row.append(node.val)
                    if node.right:
                        odd_stack.append(node.right)
                    if node.left:
                        odd_stack.append(node.left)
                res.append(row)
                row = []
        return res




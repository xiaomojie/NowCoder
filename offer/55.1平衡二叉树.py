"""
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。任意节点的左子树和右子树的深度差不超过1
"""

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    #  法1：利用55题，求二叉树的深度的方法，遍历树，对每个节点的左右子树求深度，看深度差是否大于1
    #  问题：会右很多重复的计算

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right) + 1

    def IsBalanced_Solution1(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    # 法2：每个节点只遍历一次，使用后续遍历的方式，每次遍历到这个节点的时候，其子节点都已经遍历完了
    def IsBalanced(self, pRoot):
        if not pRoot:
            return True, 0
        left, count_left = self.IsBalanced(pRoot.left)
        right, count_right = self.IsBalanced(pRoot.right)
        if (left and right) and abs(count_left - count_right) <= 1:
            return True, max(count_left, count_right) + 1

        else:
            return False, -1

    def IsBalanced_Solution(self, pRoot):
        res, n = self.IsBalanced(pRoot)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().IsBalanced_Solution(root))
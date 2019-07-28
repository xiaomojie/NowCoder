# -*- coding:utf-8 -*-
"""
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
前序遍历，（层序遍历应该是不行的），空节点要加上null，不然在反序列化的时候不好操作
"""
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return [None]
        return [root.val] + self.Serialize(root.left) + self.Serialize(root.right)

    # 法1：使用递归的方式构建树，对于序列s的处理就是直接将其进行截断
    def Deserialize(self, s):
        # write code here
        if not s:
            return None

        root, s = self.Deserialize_(s)
        return root

    def Deserialize_(self, s):
        if not s[0]:
            return None, s[1:]

        root = TreeNode(s[0])
        s = s[1:]
        root.left, s = self.Deserialize_(s)
        root.right, s = self.Deserialize_(s)

        return root, s

    # 法2：直接设置一个下标变量index来记录当前读到s的位置
    index = 0
    def Deserialize1(self, s):
        if not s:
            return None
        return self.Deserialize_(s)

    def Deserialize_1(self, s):
        if not s[self.index]:
            self.index += 1
            return None

        root = TreeNode(s[self.index])
        self.index += 1

        root.left = self.Deserialize_(s)
        root.right= self.Deserialize_(s)

        return root

print(Solution().Deserialize([1,2,None,None,3,None,None]))
"""
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # 分三种情况讨论：
        # 1. 若该节点有右节点，则返回右节点最下面的左节点
        # 2. 若该节点没有右节点，且其为其父节点的左节点，则返回其父节点
        # 3. 若该节点为其父节点的右节点，则沿着指向父节点的指针一直往上找，直到
        #  找到一个是它父节点的左子节点的节点
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        elif pNode.next and pNode.next.left == pNode:
            return pNode.next
        else:
            while pNode.next:
                if not pNode.next.next:
                    return None
                elif pNode.next.next.left == pNode.next:
                    return pNode.next.next
                else:
                    pNode = pNode.next

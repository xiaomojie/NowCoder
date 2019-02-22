"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead1(self, listNode):
        # 法一：不该变链表结构，使用栈
        stack = []
        p = listNode
        while p:
            stack.append(p.val)
            p = p.next
        return stack[::-1]
        # stack.reverse()
        # return stack

    def printListFromTailToHead2(self, listNode):
        # 法二：不改变链表结构，使用递归，递归本质上是一个栈结构
        res = []
        if not listNode:
            return res
        tail = self.printListFromTailToHead(listNode.next)
        res += tail
        res.append(listNode.val)
        return res

    def printListFromTailToHead(self, listNode):
        # 法三：改变链表结构，把链表进行reverse，使用迭代
        pre = None
        while listNode:
            next = listNode.next
            listNode.next = pre
            pre = listNode
            listNode = next
        res = []
        while pre:
            res.append(pre.val)
            pre = pre.next
        return res


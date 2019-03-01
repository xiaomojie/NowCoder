# -*- coding:utf-8 -*-
"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
思路：有循环和递归两种实现方式
鲁棒性：输入为空；输入只包含一个节点
"""
class Solution:
    # 返回ListNode
    def ReverseList1(self, pHead):
        # 循环
        if not pHead or not pHead.next:
            return pHead
        pre = None
        cur = pHead
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def ReverseList(self, pHead):
        # 递归
        if not pHead or not pHead.next:
            return pHead
        pre = None
        return self.ReverseListRecursion(pre, pHead)

    def ReverseListRecursion(self, pre, cur):
        if not cur:
            return pre
        node = cur.next
        cur.next = pre
        pre = cur
        return self.ReverseListRecursion(pre, node)


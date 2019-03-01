# -*- coding:utf-8 -*-
"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge1(self, pHead1, pHead2):
        # 法一：递归
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            head = pHead1
            head.next = self.Merge(pHead1.next, pHead2)
        else:
            head = pHead2
            head.next = self.Merge(pHead1, pHead2.next)
        return head

    def Merge(self, pHead1, pHead2):
        # 循环
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        head = p = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                p.next = pHead1
                p = p.next
                pHead1 = pHead1.next
            else:
                p.next = pHead2
                p = p.next
                pHead2 = pHead2.next
        p.next = pHead1 or pHead2
        return head.next


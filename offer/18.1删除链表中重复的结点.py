# -*- coding:utf-8 -*-
"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        #
        if not pHead:
            return None
        p = pre = ListNode(0)
        pre.next = pHead
        while pHead and pHead.next:
            if pHead.next.val == pHead.val:
                while pHead.next and pHead.next.val == pHead.val:
                    pHead.next = pHead.next.next
                pHead = pHead.next
                pre.next = pHead
            else:
                pre = pre.next
                pHead = pHead.next
        return p.next
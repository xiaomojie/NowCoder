# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
题目描述
输入两个链表，找出它们的第一个公共结点。
'''
class Solution:
    # o(m + n)
    def FindFirstCommonNode1(self, pHead1, pHead2):
        # write code here
        p = pHead1
        q = pHead2

        n1, n2 = 0, 0
        while p:
            p = p.next
            n1 += 1
        while q:
            q = q.next
            n2 += 1
        if n1 > n2:
            diff = n1 - n2
            p, q = pHead1, pHead2
            while diff:
                p = p.next
                diff -= 1
        else:
            diff = n2 - n1
            p, q = pHead1, pHead2
            while diff:
                q = q.next
                diff -= 1
        while p and q:
            if p == q:
                return p
            p = p.next
            q = q.next

    # o(m + n)
    def FindFirstCommonNode(self, pHead1, pHead2):
        p, q = pHead1, pHead2
        while p and q:
            if p == q:
                return p
            if not p.next:
                p = pHead2
                q = q.next
                continue
            if not q.next:
                q = pHead1
                p = p.next
                continue
            p = p.next
            q = q.next

    # 还可以使用两个栈，保存两个链表，然后弹出比较


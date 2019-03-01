# -*- coding:utf-8 -*-
"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
1. 是否存在环  2. 环入口
思路1：首先设置一个slow和一个fast指针，slow每次走一步，fast每次走两步，若相遇了，则说明一定存在环
然后设置指针p从头出发，slow 从相遇点继续走，在p和slow会在入口相遇

思路2：设置slow和fast判断是否存在环，然后统计出环中节点个数，然后再来两个指针p和q从头开始，p先走n步，
然后q以相同的速度来追，则追上点为入口

鲁棒性：输入头为空；不存在环
"""
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        slow = fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 相遇
                p = pHead
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        else:  # 不存在环
            return None

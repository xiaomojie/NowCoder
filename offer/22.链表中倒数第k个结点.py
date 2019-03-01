# 方法1.把链表反转，然后在从后往前，但是改变了链表的结构
# 方法2.先遍历一遍链表，统计出一个有多少节点n，然后倒数第k个节点就是从头开始数第n-k+1个节点，再遍历一遍就行了
# 方法3.设置两个变量，left和right，中间相差k，当right到达末尾时，left到达倒数第k个
# 要考虑代码的鲁棒性：a.输入的为空指针  b.输入的链表总节点数小于k   c.输入的k为0


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k < 1:
            return None
        slow = fast = head
        for i in range(k - 1):
            if not fast.next:
                return None
            else:
                fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
print(Solution().FindKthToTail(a, 1))

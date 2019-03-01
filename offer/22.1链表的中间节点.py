"""
求链表的中间节点，如果链表中的节点综述为奇数，则返回中间节点，如果节点综述是偶数，则返回中间两个节点的任意一个
"""
# 思路：设计两个指针，一个每次走一步，另一个每次走两步
# 鲁棒性：输入的链表为空则返回空；
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def find_middle(self, head):
        if not head:
            return None
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print(Solution().find_middle(a).val)
print(Solution().find_middle(None))

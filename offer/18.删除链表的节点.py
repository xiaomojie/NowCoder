"""
在O(1)时间内删除链表节点
给定单项链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def delete_node(self, head, node):
    # 最容易想到的方法就是从头往后遍历，是因为要得到被删除节点的前一个节点，但是时间是O（n）
    # 其实也可以把被删除节点的后一个节点的内容复制到要删除的节点上，然后删除下一个节点，不过
    # 这样就改变了链表的原始结构了（并不算），但是复杂度为O（1）
    # 此时还要考虑一些特殊情况：
    # 1. 删除的是尾节点，此时下一个节点为空，此时就只能从头遍历了
    # 2. 只有一个节点，且要删除这个节点，即删除头结点/尾节点，删除这个节点且将头结点设为空
        if not head or not node:
            return
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        elif not head.next and head == node:
            head = None

        else:
            p = head
            while p.next != node:
                p = p.next
            p.next = None

        return head

p = head = ListNode(1)
# print(head.val, head.next)
p.next = ListNode(2)
# print(head.val,head.next.val, head.next)
p = p.next
p.next = ListNode(3)
# print(head.val, head.next.val, head.next.next.val, head.next.next)
p = p.next
p.next = ListNode(4)
p = p.next
# print(head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next)

head = Solution().delete_node(head, p)
while head:
    print(head.val)
    head = head.next


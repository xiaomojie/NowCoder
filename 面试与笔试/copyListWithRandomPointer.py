# Leetcode 138:对一个有随机指针的链表进行深拷贝
class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        p = q = head
        node_dict = {}
        while p:
            node_dict[p] = RandomListNode(p.val)
            p = p.next

        while q:
            node_dict[q].next = node_dict[q.next]
            node_dict[q].random = node_dict[q.random]
            q = q.next

        return node_dict[head]
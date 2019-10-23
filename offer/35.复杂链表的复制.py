# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    # 法一：先复制链表，然后再对每一个节点设置random指针，由于random指针指向的位置不确定，所以得
    # 从原始链表的头部开始，走s部，到达所指向的节点，那么在新链表中也走s步，time:O(N^2),space:O(1)

    # 法二：先复制链表，但复制每个节点的同时把random信息存到一个hash表中，有了hash表可以再O(1)的时
    # 间找到random，time:O(n)  spacd:O(n)

    # 法三：不用辅助空间，复制节点的时候直接把节点放在被复制的节点后面，这样新节点的random可以通过
    # 原来节点找到

    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        cur = pHead
        # 先复制链表，并把新节点放在原节点后面
        while cur:
            node = RandomListNode(str(cur.label) + "*")
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        # 再遍历一次，设置random指针
        cur = pHead
        while cur:
            random = cur.random
            if random:
                cur.next.random = random.next
            cur = cur.next.next
        # 将新链表抽出来
        head = cur = pHead.next
        pHead.next = cur.next
        old = pHead.next
        while old:
            cur.next = old.next
            cur = cur.next
            old.next = cur.next
            old = old.next
        return head

# 测试：
# 1. 空
# 2. 只有一个节点
# 3. random指向节点自身
# 4. 两个节点的random形成环状

print(Solution().Clone(None))
print("______________")

a = RandomListNode(1)
a.random = a
clone_a = Solution().Clone(a)
while clone_a:
    print(clone_a.label, clone_a.next, clone_a.random.label)
    clone_a = clone_a.next
print("______________")

a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
a.next = b
a.random = c
b.next = c
b.random = b
c.random = a
cur = a
# while cur:
#     print(cur.label, cur.next, cur.random.label)
#     cur = cur.next
# print("______________")

clone_a = clone = Solution().Clone(a)
while clone_a:
    print(clone_a.label, clone_a.next, clone_a.random.label)
    clone_a = clone_a.next
print("______________")



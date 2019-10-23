class LinkNode:
    def __init__(self, x):
        self.next = None
        self.jump = None
        self.val = x

class Solution:
    # 法三：不用辅助空间，复制节点的时候直接把节点放在被复制的节点后面，这样新节点的random可以通过
    # 原来节点找到
    def clone(head):
        if not head:
            return head
        cur = head
        while cur:
            node = LinkNode(str(cur.val) + "'")
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        cur = head
        while cur:
            jump = cur.jump
            if jump:
                cur.next.jump = jump.next
            cur = cur.next.next

        new_head = cur = head.next
        old = head
        old.next = new_head.next
        old = old.next.next
        while old:
            cur.next = old.next
            cur = cur.next
            old.next = cur.next
            old = old.next
        return new_head

    # 法二：先复制链表，但复制每个节点的同时把random信息存到一个hash表中，有了hash表可以再O(1)的时
    # 间找到random，time:O(n)  spacd:O(n)
    def clone2(head):
        if not head:
            return head

        map = dict()
        cur = head
        while cur:
            node = LinkNode(str(cur.val) + "'")
            map[cur] = node
            cur = cur.next
        node = head
        while node:
            map.get(node).next = map.get(node.next)
            map.get(node).jump = map.get(node.jump)
            node = node.next
        return map.get(head)

print(Solution().Clone(None))
print("______________")

a = LinkNode(1)
a.random = a
clone_a = Solution().Clone(a)
while clone_a:
    print(clone_a.val, clone_a.next, clone_a.random.val)
    clone_a = clone_a.next
print("______________")

a = LinkNode(1)
b = LinkNode(2)
c = LinkNode(3)
a.next = b
a.random = c
b.next = c
b.random = b
c.random = a
# cur = a
# while cur:
#     print(cur.label, cur.next, cur.random.label)
#     cur = cur.next
# print("______________")

clone_a = clone = Solution().Clone(a)
while clone_a:
    print(clone_a.label, clone_a.next, clone_a.random.label)
    clone_a = clone_a.next
print("______________")




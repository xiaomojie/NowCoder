# -*- coding:utf-8 -*-
"""
定义一个队列并实现函数max得到队列的最大值，要求函数max，push_back，pop_front的时间复杂度都是O(1)
"""

"""
思路：队列的最大值，使用另外一个队列来存储最大值，当push一个值的时候，如果该值小于队尾的值时，直接放到队尾，如果大于队尾的值时，则将队尾连续
出队列，直到不大于，然后当前值入队
"""
class Queue:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def max(self):
        if self.max_queue:
            return self.max_queue[0]
        else:
            return None

    def push_back(self, x):
        self.queue.append(x)
        while self.max_queue and x > self.max_queue[-1]:
            self.max_queue.pop()
        self.max_queue.append(x)

    def pop_front(self):
        if not self.queue:
            return None
        res = self.queue[0]
        if self.max_queue[0] == res:
            self.max_queue = self.max_queue[1:]
        self.queue = self.queue[1:]
        return res

s = Queue()
print(s.pop_front())
s.push_back(3)
print(s.max())
print(s.pop_front())
s.push_back(5)
s.push_back(2)
s.push_back(4)
s.push_back(1)
print(s.max())
print(s.pop_front())
print(s.max())


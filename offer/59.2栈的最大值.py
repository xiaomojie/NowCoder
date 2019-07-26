# -*- coding:utf-8 -*-
"""
定义一个栈并实现函数max得到栈的最大值，要求函数max，push，pop的时间复杂度都是O(1)
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    def max(self):
        if not self.max_stack:
            return None
        else:
            return self.max_stack[-1]

    def push(self, x):
        self.stack.append(x)
        if self.max_stack and self.max_stack[-1] > x:
            return
        else:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        res = self.stack.pop()
        if res == self.max_stack[-1]:
            self.max_stack.pop()
        return res

s = Stack()
print(s.pop())
s.push(3)
print(s.max())
print(s.pop())
s.push(5)
s.push(2)
s.push(4)
s.push(1)
print(s.max())
print(s.pop())
print(s.max())

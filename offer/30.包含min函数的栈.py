# -*- coding:utf-8 -*-
"""
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""
class Solution:
    # 使用两个栈，一个栈是正常的，另一个用来保存最小值,每一次push的时候，判断push的值与当前stack_min的最后一个值谁更小，
    # 把更小的当做当前最小值
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.stack_min:
            self.stack_min.append(node)
        else:
            self.stack_min.append(node if node < self.stack_min[-1] else self.stack_min[-1])

    def pop(self):
        # write code here
        if self.stack is []:
            return None
        else:
            self.stack_min.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def min(self):
        # write code here
        if self.stack_min:
            return self.stack_min[-1]
        else:
            return None

s = Solution()
s.push(3)
print(s.min())
s.push(4)
print(s.min())
s.push(2)
print(s.min())
s.push(3)
print(s.min())
print(s.pop())
print(s.min())
print(s.pop())
print(s.min())
print(s.pop())
print(s.min())
s.push(0)
print(s.min())


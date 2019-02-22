"""
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


# -*- coding:utf-8 -*-
class Solution:
    # 思路：入列时往stack1中放，出列时从stack2中出，若stack2为空，则将stack1中的
    # 内容全部弹出到stack2中，然后再从stack2中出
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        else:
            if self.stack1:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
            else:
                return None



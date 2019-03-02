# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []

    def IsPopOrder(self, pushV, popV):
        # 遍历popV中的每一个元素，如果该元素与当前栈顶的元素相同，则弹出，如果不相同，
        # 则pushv中的元素继续入栈
        for k in popV:
            if not self.stack or self.stack[-1] != k:
                i = 0
                while i < len(pushV):
                    if pushV[i] != k:
                        self.stack.append(pushV[i])
                        i += 1
                    else:
                        break
                if i == len(pushV):
                    return False
                else:
                    pushV = pushV[i + 1:]
            else:
                self.stack.pop()
        return True



# -*- coding:utf-8 -*-
'''
将字符串头部几个字符移到尾部
abcdef => cdefgab
'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return s
        head = self.reverse(s[0:n])
        tail = self.reverse(s[n:])
        return self.reverse(head + tail)

    def reverse(self, s):
        if not s:
            return s
        s = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)

print(Solution().LeftRotateString('abcdefg', 2))
print(Solution().LeftRotateString('abcdefg', 0))

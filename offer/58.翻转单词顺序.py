# -*- coding:utf-8 -*-
'''
输入一个英文句子，翻转句子中单词顺序，但单词内字符的顺序不变，标点符号和普通字母一样处理，例如：i am a student. => student. a am i
'''
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""
        s = self.reverse(s)
        segs = s.split(' ')
        res = []
        for seg in segs:
            res.append(self.reverse(seg))
        return ' '.join(res)

    def reverse(self, s):
        if not s:
            return ""
        s = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)

    def ReverseSentence1(self, s):
        s = s.split(' ')
        return ' '.join(s[::-1])

print(Solution().ReverseSentence('i am a student.'))
"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，
当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace1(self, s):
        # 法一：python 内置函数
        return s.replace(" ", "%20")
    def replaceSpace2(self, s):
        # 法二：利用python list
        list_s = list(s)
        for i in range(len(list_s)):
            if list_s[i] == ' ':
                list_s[i] = '%20'
        return ''.join(list_s)
    def replaceSpace(self, s):
        # 法三：list
        res = ''
        for i in range(len(s)):
            if s[i] == ' ':
                res += '%20'
            else:
                res += s[i]
        return res

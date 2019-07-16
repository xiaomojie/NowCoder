# -*- coding:utf-8 -*-

"""
在字符串中找出第一个只出现一次的字符，输入"abaccdeff"，则输出1
"""

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = dict()
        for i in range(len(s)):
            if s[i] in dic.keys():
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1

print(Solution().firstNotRepeating("abaccdeff"))
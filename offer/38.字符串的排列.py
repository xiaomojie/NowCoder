# -*- coding:utf-8 -*-
"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""


class Solution:
    def Permutation(self, ss):
        # write code here
        res = []
        if ss == '':
            return res

        ss = list(ss)
        self._Permutation(ss, 0, res)

        return sorted(res)

    def _Permutation(self, ss, begin, res):
        if begin == len(ss) - 1:
            res.append(''.join(ss))
            return

        for i in range(begin, len(ss)):
            if ss[begin] == ss[i] and begin != i:
                continue
            ss[begin], ss[i] = ss[i], ss[begin]
            self._Permutation(ss, begin + 1, res)
            ss[begin], ss[i] = ss[i], ss[begin]
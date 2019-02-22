# -*- coding:utf-8 -*-
"""
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""
class Solution:
    def Fibonacci1(self, n):
        # 法一：递归，会进行很多重复的运算，当n过大的时候速度会很慢，复杂度是
        # n的指数方式递增的，在这个问题中会time limited
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

    def Fibonacci(self, n):
        # 自下而上，把已经算好的结果保存起来，减少重复计算
        # 复杂度 O(n)
        res = [0, 1, -1]
        if n < 2:
            return res[n]
        for i in range(2, n + 1):
            res[2] = res[0] + res[1]
            res[0] = res[1]
            res[1] = res[2]
        return res[2]

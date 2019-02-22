# -*- coding:utf-8 -*-
"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少
种跳法（先后次序不同算不同的结果）。
"""
class Solution:
    def jumpFloor(self, number):
        # 是斐波那契数列问题的变种，如果只有一级台阶，1种跳法，2级，两种跳法
        # 当n>2时，第一次跳有两种跳法：
        # 1.跳一级，此时跳法数目为剩下的n-1级台阶跳法数目
        # 2.跳两级，此时跳法数目为剩下的n-2级台阶跳法数目
        # f(n) = f(n-1) + f(n-2)
        res = [1,2,-1]
        if number <= 2:
            return res[number-1]
        for i in range(3, number+1):
            res[2] = res[0] + res[1]
            res[0] = res[1]
            res[1] = res[2]
        return res[2]

    # 类似题：leetcode上91_Decode_Ways
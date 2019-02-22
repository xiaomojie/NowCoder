# -*- coding:utf-8 -*-
"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个
n级的台阶总共有多少种跳法。
"""
class Solution:
    def jumpFloorII(self, number):
        # 只有一级台阶时：1种，两级：2种f(2)=f(1)+1, 三级：f(3)=f(2)+f(1)+1=2f(2)
        # 四级：f(4)=f(3)+f(2)+f(1)+1=2f(3)=4f(2)
        # 五级：f(5)=f(4)+f(3)+f(2)+f(1)+1=2f(4)=8f(2)
        # f(n)=2f(n-1)=2^(n-2)f(2)=2^(n-1)
        res = [1,-1]
        if number == 1:
            return res[0]
        for i in range(2, number+1):
            res[1] = 2*res[0]
            res[0] = res[1]
        return res[1]
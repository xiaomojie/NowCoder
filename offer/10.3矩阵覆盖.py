# -*- coding:utf-8 -*-
"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地
覆盖一个2*n的大矩形，总共有多少种方法？
"""
class Solution:
    def rectCover(self, number):
        # 用第一个2*1的矩阵去覆盖大矩阵最左边的时候，有两种覆盖方式
        # 横着放：则左下角也只能再横着放一个2*1，所以还剩右边2*(n-2)的区域f(n-2)
        # 竖着放：则最左边的区域被占据，还剩右边n-1的区域，f(n-1)
        # f(n) = f(n-1) + f(n-2)
        if number <= 0:
            return 0
        res = [1, 2, -1]
        if number < 3:
            return res[number - 1]
        for i in range(3, number + 1):
            res[2] = res[0] + res[1]
            res[0] = res[1]
            res[1] = res[2]
        return res[2]

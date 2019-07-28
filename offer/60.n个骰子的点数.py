# -*- coding:utf-8 -*-

"""
把n个骰子仍在地上，所有骰子朝上一面的点数只和为s，输入n，打印出s的所有可能的值出现的概率
"""
import math
MAX_VALUE = 6
class Solution:
    def propobility(self, n):
        if n < 1:
            return
        prob = [[0]*(MAX_VALUE * n + 1) for i in range(2)]
        flag = 0
        for i in range(1, MAX_VALUE + 1):
            prob[flag][i] = 1

        for k in range(2, n + 1):
            for i in range(0, k):
                prob[1 - flag][i] = 0

            for i in range(k, MAX_VALUE * k + 1):
                prob[1 - flag][i] = 0
                j = 1
                while j < i and j <= MAX_VALUE:
                    prob[1-flag][i] += prob[flag][i-j]
                    j += 1

            flag = 1 - flag

        # 最后的值就存在prob[flag]中，求概率
        # total = math.pow(6, n)
        # for i in range(MAX_VALUE * n + 1):
        #     prob[flag][i] /= float(total)
        return prob[flag]

print(Solution().propobility(2))


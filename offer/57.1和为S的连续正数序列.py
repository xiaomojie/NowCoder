# -*- coding:utf-8 -*-
'''
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

输入一个正整数s，打印所有和为s的连续正数序列（至少包含有两个数），例如输入15，由于1+2+3+4+5 = 4+5+6 = 7+8 = 15，所以打印出三个连续序列
1～5，4～6，7～8
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        if tsum < 3:
            return res
        small = 1
        big = 2
        cur_sum = small + big
        while small <= (tsum + 1) // 2:
            if cur_sum == tsum:
                res.append(range(small, big+1))
                big += 1
                cur_sum += big
            elif cur_sum > tsum:
                cur_sum -= small
                small += 1
            else:
                big += 1
                cur_sum += big
        return res

print(Solution().FindContinuousSequence(15))
print(Solution().FindContinuousSequence(3))
print(Solution().FindContinuousSequence(0))
print(Solution().FindContinuousSequence(4))
print(list(range(1,3)))
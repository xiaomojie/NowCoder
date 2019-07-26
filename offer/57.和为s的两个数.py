'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array or len(array) < 2:
            return []
        left, right = 0, len(array) - 1
        while left < right:
            s = array[left] + array[right]
            if s == tsum:
                return array[left], array[right]
            elif s > tsum:
                right -= 1
            else:
                left += 1

        return []

print(Solution().FindNumbersWithSum([1,2,4,7,11,16],10))

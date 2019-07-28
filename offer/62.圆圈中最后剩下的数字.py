# -*- coding:utf-8 -*-
"""
0，1，2...n-1这n个数排成一个圆圈，从数字0开始，每次从这个圆圈中删除第m个数字，求出这个圆圈理剩下的最后一个数字
"""
'''
思路：使用一个list来模拟一个圆圈，每次删去一个，然后再按正确的顺序拼接一下
'''
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        queue = []
        for i in range(n):
            queue.append(i)

        cur = 0
        while len(queue) > 1:
            remove = (cur + m - 1) % len(queue)
            queue = queue[remove + 1:] + queue[:remove]
            cur = 0
        return queue[0]

print(Solution().LastRemaining_Solution(5, 3))
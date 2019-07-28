# -*- coding:utf-8 -*-
"""
从一副扑克牌中抽5张，判断这五张是否是连续的，2～10为数字本身，A为1，J为11，Q为12，K为13，大小王为可以变成
"""

'''
思路：输入的就是数字，0表示的是大小王，首先先对数组排一个序，然后统计0的个数，然后在遍历数组统计gap的个数，
如果前一个元素和后一个元素相等，那么直接返回false，如果不想等则计算gap值，最后比较0的个数是不是大于等于gap值。
'''
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()

        count_0 = 0
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            count_0 += 1
            i += 1

        small = count_0
        big = small + 1
        count_gap = 0
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            count_gap = count_gap + numbers[big] - numbers[small] - 1
            small = big
            big += 1

        return count_0 >= count_gap


print(Solution().IsContinuous([1,3,2,5,4]))
print(Solution().IsContinuous([3,5,0,6,0]))
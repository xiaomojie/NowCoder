# -*- coding:utf-8 -*-
'''
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array) < 2:
            return None
        xor_sum = 0
        for item in array:
            xor_sum ^= item

        # 找到一位为1的,下面这种方法是错误的，这里是十进制表示的！！
        # index = 0
        # for i in range(len(str(xor_sum)) - 1, -1, -1):
        #     if str(xor_sum)[i] == '1':
        #         index = i - len(str(xor_sum))
        #         break
        # if index == 0:
        #     return None

        # 找到一位为1的
        index = self.find_first_1bit(xor_sum)

        # 分成两组
        group1 = 0
        group2 = 0
        for i in range(len(array)):
            if self.is_bit1(array[i], index):
                group1 ^= array[i]
            else:
                group2 ^= array[i]
        return group1, group2

    def find_first_1bit(self, xor_sum):
        index = 0
        while xor_sum:
            xor_sum = xor_sum >> 1
            index += 1
        return index

    def is_bit1(self, num, index):
        num = num >> (index - 1)
        return num & 1

print(Solution().FindNumsAppearOnce([1,2]))
print(Solution().FindNumsAppearOnce([1,1,2,2,3,4,4,5,6,6]))

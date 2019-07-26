# -*- coding:utf-8 -*-
'''
题目描述
在一个数组中除一个数字只出现一次外，其他都出现了三次，找出这个只出现一次的
'''


#  负数会出问题
class Solution:
    # 如果一个数字出现三次，那么它的二进制表示的每一位（0或1）也出现三次，如果把所有出现三次的数字的二进制表示的每一位
    # 都分别加起来，那么每一位的和都能被3整除
    def FindNumsAppearOnce(self, array):
        if not array:
            return None

        bit_sum = [0] * 32
        for i in range(len(array)):
            tmp = array[i]
            index = 0
            while tmp:
                if tmp & 1:
                    bit_sum[index] += 1
                tmp = tmp >> 1
                index += 1

        res = 0
        # print(bit_sum)
        for i in range(len(bit_sum)-1, -1, -1):
            # res = res << 1
            # res += bit_sum[i] % 3
            res = (res << 1) + bit_sum[i] % 3
            # print(res)


        return res

print(Solution().FindNumsAppearOnce([1,2,3,1,1,2,2,4,4,4]))
print(Solution().FindNumsAppearOnce([]))
print(Solution().FindNumsAppearOnce([1]))
print(Solution().FindNumsAppearOnce([0,1,1,1]))
print(Solution().FindNumsAppearOnce([-1,1,1,1]))
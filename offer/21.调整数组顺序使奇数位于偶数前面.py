# -*- coding:utf-8 -*-
# 法一：从前往后扫描，每遇到一个偶数，则把其后面的数都往前移一位，然后把这个偶数放到最后，复制度为O（n^2）

# 可以把判断是否是奇数的部分提出来写一个单独的函数，这样可扩展

class Solution:
    def reOrderArray1(self, array):
        # 法二: 这种方法不能保证奇数和奇数，偶数和偶数之间的相对位置不变
        # 设置两个指针，一个指向头部，一个指向尾部，然后向内移动，
        # 分别找到一个奇数一个偶数，然后调换位置
        if array is None:
            return
        low = 0
        high = len(array)-1
        while low < high:
            while low < high and array[low] % 2 != 0:
                low += 1
            while low < high and array[high] % 2 == 0:
                high -= 1
            if low < high:
                array[low], array[high] = array[high], array[low]
        return array
    def reOrderArray(self, array):
        # 更简单的方法，但是占内存
        odd = [item for item in array if item % 2 == 1 ]
        even = [item for item in array if item % 2 == 0]
        return odd + even

    def reOrderArray2(self, array):
        # 为了保证相对位置不变
        if not array:
            return array
        low = 0
        while low < len(array):
            while low < len(array) and array[low] % 2 != 0:
                low += 1
            high = low + 1
            while high < len(array) and array[high] % 2 == 0:
                high += 1
            if high < len(array):
                # array[low], array[high] = array[high], array[low]  这里不能用交换，结果不对
                array.insert(low, array.pop(high))
                low += 1
            else:
                break
        return array

array = [1,2,3,4,5,6,7]
Solution().reOrderArray(array)
print(array)
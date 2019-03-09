# -*- coding:utf-8 -*-
import collections
class Solution:
    def MoreThanHalfNum_Solution2(self, numbers):
        # 法一：使用Partition
        if not numbers:
            return False
        mid = len(numbers) // 2
        low = 0
        high = len(numbers) - 1
        index = self.partition(numbers, low, high)
        while index != mid:
            if index > mid:
                high = index - 1
                index = self.partition(numbers, low, high)
            else:
                low = index + 1
                index = self.partition(numbers, low, high)

        # 判断是否超过了一半
        res = numbers[mid]
        i = 0
        count = 0
        while i < len(numbers):
            if numbers[i] == res:
                count += 1
            i += 1
        if count * 2 <= len(numbers):
            return 0
        return res

    def partition(self, number, low, high):
        pivot = number[low]
        while low < high:
            while low < high and number[high] > pivot:
                high -= 1
            number[low] = number[high]
            while low < high and number[low] <= pivot:
                low += 1
            number[high] = number[low]
            # print(number)
        number[low] = pivot
        return low

    def MoreThanHalfNum_Solution(self, numbers):
        # 法二：根据数组特点，存储数字和其出现的次数，遍历，如果下一个出现的与当前保存的
        # 数字相同，则次数加一，如果不相同则次数减一，如果为0则需要保存下一个数字
        if not numbers:
            return 0
        key = numbers[0]
        num = 1
        for i in range(1,len(numbers)):
            if num == 0:
                key = numbers[i]
                num = 1
            elif numbers[i] == key:
                num += 1
            else:
                num -= 1
        # 判断是否存在出现多余一半的
        i = 0
        count = 0
        while i < len(numbers):
            if numbers[i] == key:
                count += 1
            i += 1
        if count * 2 > len(numbers):
            return key
        else:
            return 0

    def MoreThanHalfNum_Solution1(self, numbers):
        # 法三：使用partion
        c = collections.Counter(numbers)
        for k, v in c.items():
            if v > len(numbers) / 2:
                return k
        return 0

    def MoreThanHalfNum_Solution3(self, numbers):
        # 法四：使用dict
        d = {}
        for item in numbers:
            if item not in d.keys():
                d[item] = 1
            else:
                d[item] += 1
            if d[item] > len(numbers)/2:
                return item
        return 0




# print(Solution().MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))
# print(Solution().MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))
# print(Solution().MoreThanHalfNum_Solution([1,1,1,1]))
# print(Solution().MoreThanHalfNum_Solution([1,2,3,4]))
print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
print(Solution().MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))

# coding = utf-8

'''
题目描述
统计一个数字在排序数组中出现的次数。
'''


class Solution:
    def GetNumberOfK(self, data, k):
        left = 0
        right = len(data) - 1
        leftk = self.getleftK(data, k, left, right)
        rightk = self.getrightK(data, k, left, right)
        return rightk - leftk + 1

    def getleftK(self, data, k, left, right):###查找重复数字中最左边的那个数字位置
        while left <= right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getrightK(self, data, k, left, right):###查找重复数字最右边的那个数字位置
        while left <= right:
            mid = (left + right) // 2
            if data[mid] <= k:
                left = mid + 1
            else:
                right = mid - 1
        return right

print(Solution().GetNumberOfK([1,2,3,3,3,4], 2))



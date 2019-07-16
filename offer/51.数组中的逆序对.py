# -*- coding:utf-8 -*-
class Solution:
    # 两个数组从后往前合并
    def merge1(self, left, right):
        i, j = len(left) - 1, len(right) - 1
        res = []
        count = 0
        while i >= 0 and j >= 0:
            if left[i] <= right[j]:
                res = [right[j]] + res
                j -= 1
            else:
                res = [left[i]] + res
                count = count + (j + 1)
                i -= 1
        res = (left[:i+1] or right[:j+1]) + res
        return res, count

        # 两个数组从前往后合并
    def merge(self, left, right):
        i, j = 0, 0
        res = []
        count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                count += (len(left) - i)
                j += 1
        res += left[i:] or right[j:]
        return res, count

    def sort(self, data):
        # write code here
        if not data or len(data) <= 1:
            return data, 0

        mid = len(data) // 2
        left, n1 = self.sort(data[:mid])
        right, n2 = self.sort(data[mid:])
        res, n3 = self.merge(left, right)
        return res, n1 + n2 + n3

    def InversePairs(self, data):
        if not data:
            return 0
        res, count = self.sort(data)
        return count

if __name__ == '__main__':
    print(Solution().InversePairs([1,3,2,3,1]))
    print(Solution().InversePairs([1,3,2,1]))
    print(Solution().InversePairs([1,2,3,4,5,6,7,0]))


# 用python总是会超时，有博客说用java不会
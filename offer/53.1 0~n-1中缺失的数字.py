'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且都在0~n-1的范围内，这个范围内的n个数只有一个不出现在改数组中，找出这个数
'''

class Solution:

    # 不够严谨，还有些特殊情况
    def find_miss_value1(self, data):
        if not data:
            return None
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == mid:
                left = mid + 1
            elif data[mid] > mid:
                right = mid - 1
        return left

    def find_miss_value(self, data):
        if not data:
            return -1
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] != mid:
                if mid ==0 or data[mid - 1] == mid -1:
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        if left == len(data):
            return left

        return -1

print(Solution().find_miss_value([0,1,2,4,5]))
print(Solution().find_miss_value([1,2,3,4,5]))
print(Solution().find_miss_value([0,1,2,3,4]))
print(Solution().find_miss_value([0]))
print(Solution().find_miss_value([]))
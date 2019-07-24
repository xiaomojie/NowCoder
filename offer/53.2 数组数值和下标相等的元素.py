'''

'''

class Solution:
    def find_first_same(self, data):
        if not data:
            return -1
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == mid:
                return mid
            elif data[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return -1

print(Solution().find_first_same([]))
print(Solution().find_first_same([0]))
print(Solution().find_first_same([1]))
print(Solution().find_first_same([-3,-2,0,1,4,5]))
print(Solution().find_first_same([0,2,4,5]))
print(Solution().find_first_same([-4,-2,2]))
print(Solution().find_first_same([-4,-2,-3,0,1]))
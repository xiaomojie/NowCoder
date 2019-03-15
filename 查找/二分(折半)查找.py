class Solution:
    def binary_search(self, num, target):
        if not num:
            return False
        low = 0
        high = len(num) - 1
        while low <= high:
            mid = (low + high) >> 1
            if num[mid] == target:
                return mid
            elif num[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

print(Solution().binary_search([5,13,19,21,37,56,64,75,80,88,92],21))
print(Solution().binary_search([5,13,19,21,37,56,64,75,80,88,92],85))

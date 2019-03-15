# time: O(n^2)
class Solution:
    def binary_insert_sort(self, nums):
        for i in range(1, len(nums)):
            low = 0
            high = i-1
            while low <= high:
                mid = (low + high) >> 1
                if nums[mid] == nums[i]:
                    high = mid
                    break
                elif nums[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid - 1
            tmp = nums[i]
            for j in range(i-1, high, -1):
                nums[j+1] = nums[j]
            nums[high + 1] = tmp
        return nums

nums = []
print(Solution().binary_insert_sort(nums))
nums = [1]
print(Solution().binary_insert_sort(nums))
nums = [1,2,3]
print(Solution().binary_insert_sort(nums))
nums = [4,3,2,1]
print(Solution().binary_insert_sort(nums))
nums = [3,1,2,4,3,0]
print(Solution().binary_insert_sort(nums))
nums = [1,4,5,6,3,4]
print(Solution().binary_insert_sort(nums))


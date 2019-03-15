# time: O(n^2)
# 最好移动次数：0
# 最差移动次数：n-1
# 无论好坏，比较次数均为 n(n-1)/2
class Solution:
    def select_sort(self, nums):
        for i in range(len(nums)):
            min_num = nums[i]
            index = i
            for j in range(i+1, len(nums)):
                if nums[j] < min_num:
                    min_num = nums[j]
                    index = j
            nums[i], nums[index] = nums[index], nums[i]
        return nums

nums = []
print(Solution().select_sort(nums))
nums = [1]
print(Solution().select_sort(nums))
nums = [1,2,3]
print(Solution().select_sort(nums))
nums = [4,3,2,1]
print(Solution().select_sort(nums))
nums = [3,1,2,4,3,0]
print(Solution().select_sort(nums))
nums = [1,4,5,6,3,4]
print(Solution().select_sort(nums))

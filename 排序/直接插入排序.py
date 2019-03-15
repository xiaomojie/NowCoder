# time: O(n^2)
# 最好比较次数：n-1
# 最好移动次数：0
# 最坏比较次数：(n+2)(n-1)/2
# 最坏移动次数：(n+4)(n-1)/2
class Solution:
    def insertSort(self, nums):
        if not nums:
            return nums
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                tmp = nums[i]
                j = i - 1
                while j >= 0 and nums[j] > tmp:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = tmp
        return nums

# nums = []
# print(Solution().insertSort(nums))
# nums = [1]
# print(Solution().insertSort(nums))
# nums = [1,2,3]
# print(Solution().insertSort(nums))
# nums = [4,3,2,1]
# print(Solution().insertSort(nums))
# nums = [3,1,2,4,3,0]
# print(Solution().insertSort(nums))
nums = [1,4,5,6,3,4]
print(Solution().insertSort(nums))
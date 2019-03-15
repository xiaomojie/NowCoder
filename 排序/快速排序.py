# 快速排序的平均时间复杂度为O(nlogn)
# 在最坏的情况下，有序的情况，快速排序可退化成冒泡排序，最坏时间复杂度为O(n^2),
# 可以依照nums[low], nums[mid], nums[high]三者取中的法则来选取pivot
# 需要一个栈空间来实现递归，空间复杂度O(logn)
class Solution:
    def Partition(self, nums, low, high):
        pivotkey = nums[low]
        while low < high:
            while low < high and nums[high] >= pivotkey:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivotkey:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivotkey
        print(nums)
        return low

    def QuickSort(self, nums, low, high):
        if low < high:
            partition = self.Partition(nums, low, high)
            self.QuickSort(nums, low, partition-1)
            self.QuickSort(nums, partition+1, high)
        else:
            return

# nums = [49, 38, 65, 97, 76, 13, 27, 49]
nums = [1,2,3,1,3,4,2,4,5,6,3]
low = 0
high = len(nums)-1
Solution().QuickSort(nums, low, high)
print(nums)
# 不对
class Solution:
    def partition(self, nums, low, high):
        if not nums:
            return False
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low

    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or len(tinput) == 0 or k > len(tinput):
            return []
        start = 0
        end = len(tinput) - 1
        index = self.partition(tinput, start, end)
        while index != k - 1:
            if index < k - 1:
                start = index + 1
                index = self.partition(tinput, start, end)
            else:
                end = index - 1
                index = self.partition(tinput, start, end)
        # res = []
        # for i in range(k):
        #     res.append(tinput[i])
        return tinput[0:k]

print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))
print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],10))

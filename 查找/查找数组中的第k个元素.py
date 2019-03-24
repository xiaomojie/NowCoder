class Solution:
    def partition(self, nums, low, high):
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

    def find(self, nums, low, high, k):
        pivot = self.partition(nums, low, high)
        if pivot + 1 == k:
            return nums[pivot]
        elif pivot + 1 > k:
            return self.find(nums, low, pivot-1, k)
        else:
            return self.find(nums, pivot+1, high, k)

    def findKth(self, nums, k):
        if k < 0 or not nums:
            return False
        return self.find(nums, 0, len(nums)-1, k)

    # 迭代法
    def findKthCirculation(self, nums, k):
        if not nums or k < 0 or k > len(nums):
            return
        start = 0
        end = len(nums)-1
        index = self.partition(nums, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition(nums, start, end)
            else:
                start = index + 1
                index = self.partition(nums, start, end)
        # 下面三行求最小的k个数
        # res = []
        # for i in range(0, k):
        #     res.append(nums[i])

        res = nums[index]
        return res




print(Solution().findKth([1,2,3,2,2,5],4))
print(Solution().findKthCirculation([1,2,3,2,2,5],4))
print(Solution().findKth([1,1,1,1,1,1,1,1,11,0],4))
print(Solution().findKthCirculation([1,1,1,1,1,1,1,1,11,0],4))
print(Solution().findKth([1,2,3,4,5,6,0],4))
print(Solution().findKthCirculation([1,2,3,4,5,6,0],4))
print(Solution().findKth([6,3,5,1,2,4,7,8,9,10],4))
print(Solution().findKthCirculation([6,3,5,1,2,4,7,8,9,10],4))
print(Solution().findKth([6,3,5,1,2,4,7,8,9,10],7))
print(Solution().findKthCirculation([6,3,5,1,2,4,7,8,9,10],7))
print(Solution().findKth([6,3,5,1,2,4,7,8,9,10,0],9))
print(Solution().findKthCirculation([6,3,5,1,2,4,7,8,9,10,0],9))

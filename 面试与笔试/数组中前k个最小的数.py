# 法1：使用快排
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

    # def quick_sort_for_topk(self, nums, k, low, high):
    #     if low < high:
    #         pivot = self.partition(nums, low, high)
    #         if pivot + 1 == k:
    #             return nums[0:pivot+1]
    #         elif pivot + 1 > k:
    #             self.quick_sort_for_topk(nums[low:pivot], k, low, pivot-1)
    #         else:
    #             self.quick_sort_for_topk(nums[pivot+1:high+1], k-pivot-1, pivot+1, high)
    def quick_sort_for_topk(self, nums, k, low, high):
        pivot = self.partition(nums, low, high)
        if pivot + 1 == k:
            return nums[0:pivot + 1]
        elif pivot + 1 > k:
            return self.quick_sort_for_topk(nums, k, low, pivot-1)
        else:
            return self.quick_sort_for_topk(nums, k, pivot+1, high)

    def GetLeastNumbers_Solution(self, nums, k):
        if not nums or len(nums) < 1 or k > len(nums) or k <= 0:
            return []
        return sorted(self.quick_sort_for_topk(nums, k, 0, len(nums)-1)) # nowcoder上面要求输出的也是有序的

# 使用堆，不对
class Solution2:
    def adjust_down(self, nums, k, size):
        root = nums[k]
        i = 2 * k + 1
        while i < (size):
            if i + 1 < size and nums[i] < nums[i+1]:
                i += 1
            if root >= nums[i]:
                break
            else:
                nums[k] = nums[i]
                k = i
            i = i * 2 + 1
        nums[k] = root

    def build_max_heap(self, nums, k):
        size = (k-1) // 2
        for i in range(size, -1, -1):
            self.adjust_down(nums, i, k)

    def GetLeastNumbers_Solution(self, nums, k):
        if k == len(nums): return nums
        if k > len(nums) or k <= 0: return []
        self.build_max_heap(nums[0:k], k)
        for i in range(k, len(nums)):
            if nums[i] < nums[0]:
                nums[0] = nums[i]
                self.adjust_down(nums[0:k], 0, k)
        return nums[0:k]


# print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))
print(Solution2().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))
print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 6))
print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],10))

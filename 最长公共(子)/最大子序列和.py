class Solution:
    def max_sub_sum(self, nums):
        max_sum = 0
        now_sum = 0
        for i in range(len(nums)):
            now_sum += nums[i]
            if now_sum > max_sum:
                max_sum = now_sum
            elif now_sum < 0:
                now_sum = 0
        return max_sum

print(Solution().max_sub_sum([1,2,3,4,5,6,-5,4,-7]))
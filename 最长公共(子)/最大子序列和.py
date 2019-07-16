"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
"""
dp:
dp[i]=nums[i] if dp[i-1]<0 or i = 0
      nums[i] + dp[i-1]  if i!= 0 and dp[i-1] > 0
"""
class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        now_sum = 0
        for i in range(len(nums)):
            now_sum += nums[i]
            if now_sum > max_sum:
                max_sum = now_sum
            if now_sum < 0:
                now_sum = 0
        return max_sum
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxSum = current = nums[0]
        for n in nums[1:]:
            current = max(current + n, n)
            maxSum = max(maxSum, current)
        return maxSum

print(Solution().maxSubArray([-1,2,3,4,5,6,-5,4,-7]))
print(Solution().maxSubArray([-1]))
print(Solution().maxSubArray([-2,1]))
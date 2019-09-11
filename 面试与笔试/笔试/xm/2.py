"""
最长连续子序列的和
"""
import sys
class Solution(object):
    def max_sub_array(self, nums):
        if not nums:
            return 0
        res = tmp = nums[0]
        for n in nums[1:]:
            tmp = max(tmp + n, n)
            res = max(res, tmp)
        return res

nums = list(map(int, sys.stdin.readline().strip().split(" ")))
print(Solution().max_sub_array(nums))
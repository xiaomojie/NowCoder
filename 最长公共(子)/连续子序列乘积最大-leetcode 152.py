class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_dp = nums[0]
        min_dp = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            tmpmax = max_dp * nums[i]
            tmpmin = min_dp * nums[i]

            if tmpmax < tmpmin:
                tmpmax, tmpmin = tmpmin, tmpmax

            max_dp = max(tmpmax, nums[i])
            min_dp = min(tmpmin, nums[i])

            res = max(res, max_dp)
        return res

# https://blog.csdn.net/qq_35082030/article/details/79975912


print(Solution().maxProduct([2,3,-2,4]))
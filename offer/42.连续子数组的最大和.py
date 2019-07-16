# -*- coding:utf-8 -*-
'''
dp:
dp[i]=nums[i] if dp[i-1]<0 or i = 0
      nums[i] + dp[i-1]  if i!= 0 and dp[i-1] > 0
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        currmax = 0
        resmax = float("-inf")
        for i in range(len(array)):
            currmax = max(array[i], currmax + array[i])
            # print(currmax)
            resmax = max(resmax, currmax)
            # print(resmax)
        return resmax

print(Solution().FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))
print(Solution().FindGreatestSumOfSubArray([-2,-8,-1,-5,-9]))
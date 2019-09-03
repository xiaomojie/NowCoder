#coding=utf-8
import sys

def max_seq(nums):
    dp = [float("-inf")] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1] + nums[i]
    max_len = 0
    dic = {}
    for j in range(len(dp)):
        if dp[j] in dic.keys():
            max_len = max(max_len, j - dic[dp[j]])
        else:
            if dp[j] == 0:
                dic[dp[j]] = -1
            else:
                dic[dp[j]] = j
    return max_len

print(max_seq([1,-1,1,-1,0,5]))
print(max_seq([1,-1,1,-1,1,-1,1,-1]))
print(max_seq([1,1,-1,1,1,-1,-1]))


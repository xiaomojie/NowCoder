"""
动态规划：
dp[i][j]表示以str1[i]和str2[j]为结尾的公共子串的长度
转移方程：
            0                   if i =0 or j = 0
dp[i][j] =  dp[i-1][j-1] + 1    if str1[i] = str2[j]
            0                   if str1[i] != str2[j]
"""

class Solution:
    def longest_substring(self, str1, str2):
        dp = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
        result = 0
        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    result = max(dp[i][j], result)
                else:
                    dp[i][j] = 0
        return result

print(Solution().longest_substring('abcdefg', 'xyzabcd'))
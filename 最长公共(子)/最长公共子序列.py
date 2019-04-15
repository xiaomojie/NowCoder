"""
求LCS (Longest Common Subsequence)
动态规划：
用二维数组dp[i][j]记录串x1 x2 ...xi 和 y1 y2 ... yj的LCS长度，则可得到状态转移方程
            0                           i = 0 or j
dp[i][j] = dp[i-1][j-1]                 xi = yj
           max(dp[i][j-1], dp[i-1][j])  xi != yj
"""

class Solution:
    def LSC(self, x, y):
        dp = [[0] * (len(y)+1) for i in (range(len(x) + 1))]
        for i in range(1, len(x) + 1):
            for j in range(1, len(y) + 1):
                if x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(x)][len(y)]

print(Solution().LSC('ABCBDAB', 'BDCABA'))

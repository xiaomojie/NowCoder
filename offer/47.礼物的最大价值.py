"""
在一个m*n的棋盘上，每一格都放有礼物，从棋盘的左上角开始，每次向左或者向下移动一格，直到右下角，求礼物的最大价值
"""
"""
思路：动态规划，dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
不需要使用二维数组，一维就够了：dp[i] = max(dp[i-1], dp[i]) + matrix[i][j]
"""

class Solution:
    def max_gift_value_1(self, matrix):
        # 一维数组存储
        if not matrix:
            return 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    dp[j] = matrix[i][j]
                elif i == 0:
                    dp[j] = dp[j-1] + matrix[i][j]
                elif j == 0:
                    dp[j] = dp[j] + matrix[i][j]
                else:
                    dp[j] = max(dp[j-1], dp[j]) + matrix[i][j]
        return dp[j]

    def max_gift_value_2(self, matrix):
        # 一维数组存储，更加简洁的代码
        if not matrix:
            return 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                left = 0
                up = 0
                if i > 0:
                    up = dp[j]
                if j > 0:
                    left = dp[j-1]
                dp[j] = max(left, up) + matrix[i][j]
        return dp[j]

    def max_gift_value_3(self, matrix):
        # 二维数组存储
        if not matrix:
            return 0
        dp = [[0]*len(matrix[0])] * len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                left = 0
                up = 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = max(left, up) + matrix[i][j]
        return dp[i][j]

matrix = [[1, 10, 3, 8],[12, 2, 9, 6],[5, 7, 4, 11],[3, 7, 16, 5]]
print(Solution().max_gift_value_3(matrix))
matrix = [[2,3,4]]
print(Solution().max_gift_value_1(matrix))
matrix = [[2],[3],[4]]
print(Solution().max_gift_value_1(matrix))
matrix = [[1]]
print(Solution().max_gift_value_1(matrix))
matrix = None
print(Solution().max_gift_value_1(matrix))



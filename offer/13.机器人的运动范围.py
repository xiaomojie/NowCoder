# -*- coding:utf-8 -*-
"""
题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是
不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        # 回溯
        if rows < 1 or cols < 1:
            return 0
        visited = [0] * (rows * cols)
        count = self.moving(threshold, rows, cols, 0, 0, visited)
        return count

    def moving(self, threshold, rows, cols, row, col, visited):
        count = 0
        if 0 <= row < rows and 0 <= col < cols and not visited[row * cols + col] and self.check(threshold, row, col):
            visited[row * cols + col] = True
            count = 1 + self.moving(threshold, rows, cols, row, col - 1, visited) + \
                    self.moving(threshold, rows, cols, row, col + 1, visited) + \
                    self.moving(threshold, rows, cols, row - 1, col, visited) + \
                    self.moving(threshold, rows, cols, row + 1, col, visited)
        return count

    def check(self, threshold, row, col):
        index_sum = 0
        while row:
            index_sum += row % 10
            row = row // 10
        while col:
            index_sum += col % 10
            col = col // 10
        return index_sum <= threshold

print(Solution().movingCount(1,2,2))
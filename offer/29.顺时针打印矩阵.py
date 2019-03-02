# -*- coding:utf-8 -*-
# 存在的问题，输入的是否是n*n的矩阵
class Solution:
    # matrix类型为二维列表，需要返回列表
    # 两个函数，一个用来循环，另一个用来实现打印一圈
    def printMatrix(self, matrix):
        # 通过画图可知，每一圈的开始都是(i,i)，循环的继续的条件为cols > i * 2 and rows > i * 2
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        i = 0
        while i * 2 < len(matrix) and i * 2 < len(matrix[0]):
            res += self.printMatrixInCircle(matrix, len(matrix), len(matrix[0]), i)
            i += 1
        return res

    def printMatrixInCircle(self, matrix, rows, cols, start):
        res = []
        # 从左到右打印一行
        for i in range(start, cols-start):
            res.append(matrix[start][i])
        # 从上到下打印一列
        if start < rows - start - 1:
            for i in range(start + 1, rows - start):
                res.append(matrix[i][cols - start -1])
        # 从右到左打印一行
        if start < cols-start - 1 and start < rows - start - 1:
            for i in range(cols-start-2, start-1, -1):
                res.append(matrix[rows - start - 1][i])
        # 从下到上打印一列
        if start < cols - start - 1 and start < rows - start - 2:
            for i in range(rows - start - 2, start, -1):
                res.append(matrix[i][start])
        return res
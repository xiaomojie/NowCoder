class Solution:
    def path(self, matrix, rows, cols, row, col):
        visited = [[False for i in range(rows)] for j in range(cols)]  # 记录是否已经路过了
        res = []  # 保存结果，在python里面将res作为下面的函数的参数是按引用传递的
        self.path_core(matrix, rows, cols, row, col, visited, res)
        return res

    def path_core(self, matrix, rows, cols, row, col, visited, res):
        has = False
        if not (0 <= row < rows) or not (0 <= col < cols):  # 判断坐标是否满足要求
            return has
        if matrix[row][col] == 1 and row != 0 and col != 0:  # 如果找到值为1的点，则成功了，说明存在路径
            res.append((row, col))  # 把改点放到res中，即终点坐标放到res里面
            return True

        if matrix[row][col] != -1 and not visited[row][col]:  # 如果可以走，且没走过
            res.append((row, col))
            visited[row][col] = True
            has = self.path_core(matrix, rows, cols, row - 1, col, visited, res) or \
                self.path_core(matrix, rows, cols, row + 1, col, visited, res) or \
                self.path_core(matrix, rows, cols, row, col - 1, visited, res) or \
                self.path_core(matrix, rows, cols, row, col + 1, visited, res)
            if not has:  # 如果不存在路径，则把先前的都弹出
                res.pop()  # 弹出最后一个元素
                visited[row][col] = True
        return has


matrix = [[1,-1,-1],[0,0,1]]
rows = len(matrix)
cols = len(matrix[0])
print(Solution().path(matrix, rows, cols, 0, 0))

matrix = [[1,-1,-1],[0,0,-1],[0,0,1]]
rows = len(matrix)
cols = len(matrix[0])
print(Solution().path(matrix, rows, cols, 0, 0))

matrix = [[1,-1,-1,0],[0,0,-1,-1],[0,0,0,0],[0,0,-1,1]]
rows = len(matrix)
cols = len(matrix[0])
print(Solution().path(matrix, rows, cols, 0, 0))
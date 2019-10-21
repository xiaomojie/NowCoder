"""
给一个m * n的01矩阵，如果矩阵中若干个1是相邻的，那么称这些1是一个相邻的“块”。求给定矩阵中块的个数
输入样例（8 * 7的01矩阵）：
0 1 1 1 0 0 1
0 0 1 0 0 0 0
0 0 0 0 1 0 0
0 0 0 1 1 1 0
1 1 1 0 1 0 0
1 1 1 1 0 0 0
0 0 0 0 1 0 1
1 0 1 1 0 1 0
该矩阵中“块”的个数就为：9
https://blog.csdn.net/y_dd6011/article/details/89715169
"""
from queue import Queue
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]
def bsf(matrix):
    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not visited[i][j] and matrix[i][j] == 1:
                res += 1
                queue = Queue()
                queue.put([i,j])
                visited[i][j] = True
                while not queue.empty():
                    index = queue.get()
                    visited[index[0]][index[1]] = True
                    for k in range(0,4):
                        tmp_x = index[0] + x[k]
                        tmp_y = index[1] + y[k]
                        if 0 <= tmp_x < len(matrix) and 0 <= tmp_y < len(matrix[0]) and not visited[tmp_x][tmp_y] and matrix[tmp_x][tmp_y]==1:
                            visited[tmp_x][tmp_y] = True
                            queue.put([tmp_x, tmp_y])
    return res

# 深度优先法1
def _dfs(matrix, vis, i, j):
        vis[i][j] = True
        for k in range(0, 4):
            tmp_x = i + x[k]
            tmp_y = j + y[k]
            if 0 <= tmp_x < len(matrix) and 0 <= tmp_y < len(matrix[0]) and not vis[tmp_x][tmp_y] and matrix[tmp_x][
                tmp_y]==1:
                _dfs(matrix, vis, tmp_x, tmp_y)
def dfs(matrix):
    vis = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not vis[i][j] and matrix[i][j] == 1:
                res += 1
                _dfs(matrix,vis, i, j)
    return res

# 深度优先法2, 不太对，不是dfs
def dfs2(matrix):
    vis = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not vis[i][j] and matrix[i][j] == 1:
                res += 1
                stack = [[i,j]]
                vis[i][j] = True
                while stack:
                    index = stack.pop()
                    for k in range(0, 4):
                        tmp_x = index[0] + x[k]
                        tmp_y = index[1] + y[k]
                        if 0 <= tmp_x < len(matrix) and 0 <= tmp_y < len(matrix[0]) and not vis[tmp_x][tmp_y] and matrix[tmp_x][tmp_y] == 1:
                            vis[tmp_x][tmp_y] = True
                            stack.append([tmp_x, tmp_y])
    return res




matrix = [[0, 1, 1, 1, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 1, 1, 0],
[1, 1, 1, 0, 1, 0, 0],
[1, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 0, 1, 0]]
print(bsf(matrix))
print(dfs(matrix))
print(dfs2(matrix))




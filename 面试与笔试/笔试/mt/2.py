import sys
class Solution:
    def print(self, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        i = 0
        while i * 2 < len(matrix) and i * 2 < len(matrix[0]):
            res += self.circle(matrix, len(matrix), len(matrix[0]), i)
            i += 1
        return res

    def circle(self, matrix, r, c, s):
        res = []
        for i in range(s, c-s):
            res.append(matrix[s][i])
        if s < r - s - 1:
            for i in range(s + 1, r - s):
                res.append(matrix[i][c - s -1])
        if s < c-s - 1 and s < r - s - 1:
            for i in range(c-s-2, s-1, -1):
                res.append(matrix[r - s - 1][i])
        if s < c - s - 1 and s < r - s - 2:
            for i in range(r - s - 2, s, -1):
                res.append(matrix[i][s])
        return res

line = list(map(int, sys.stdin.readline().strip().split(" ")))
M = line[0]
N = line[1]
matrix = []
for i in range(M):
    matrix.append(list(map(int, sys.stdin.readline().strip().split(" "))))
print(' '.join([str(x) for x in Solution().print(matrix)]))
import sys
n = input()
matrix = []
for i in range(int(n)):
    matrix.append(list(map(int, sys.stdin.readline().strip().split(' '))))

min_matrix = [[0]*len(matrix[0]) for i in range(len(matrix))]
max_matrix = [[0]*len(matrix[0]) for i in range(len(matrix))]

# print(len(matrix), )
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == 0:
            min_matrix[i][j] = matrix[i][j]
            max_matrix[i][j] = matrix[i][j]
        if j == 0:
            if matrix[i][j] == 0:
                max_matrix[i][j] = max(max_matrix[i - 1][j] * -1, max_matrix[i - 1][j + 1] * -1, min_matrix[i-1][j] * -1, min_matrix[i - 1][j + 1] * -1)
                min_matrix[i][j] = min(max_matrix[i - 1][j] * -1, max_matrix[i - 1][j + 1] * -1, min_matrix[i-1][j] * -1, min_matrix[i - 1][j + 1] * -1)
            else:
                max_matrix[i][j] = max(max_matrix[i-1][j] + matrix[i][j], max_matrix[i-1][j+1] + matrix[i][j], min_matrix[i-1][j] + matrix[i][j], min_matrix[i-1][j+1] + matrix[i][j])
                min_matrix[i][j] = min(max_matrix[i-1][j] + matrix[i][j], max_matrix[i-1][j+1] + matrix[i][j], min_matrix[i-1][j] + matrix[i][j], min_matrix[i-1][j+1] + matrix[i][j])
        elif j == len(matrix[0]) - 1:
            if matrix[i][j] == 0:
                max_matrix[i][j] = max(max_matrix[i - 1][j] * -1, max_matrix[i - 1][j - 1] * -1, min_matrix[i-1][j] * -1, min_matrix[i - 1][j - 1] * -1)
                min_matrix[i][j] = min(max_matrix[i - 1][j] * -1, max_matrix[i - 1][j - 1] * -1, min_matrix[i-1][j] * -1, min_matrix[i - 1][j - 1] * -1)
            else:
                max_matrix[i][j] = max(max_matrix[i-1][j] + matrix[i][j], max_matrix[i-1][j-1] + matrix[i][j], min_matrix[i-1][j] + matrix[i][j], min_matrix[i-1][j-1] + matrix[i][j])
                min_matrix[i][j] = min(max_matrix[i-1][j] + matrix[i][j], max_matrix[i-1][j-1] + matrix[i][j], min_matrix[i-1][j] + matrix[i][j], min_matrix[i-1][j-1] + matrix[i][j])

        else:
            if matrix[i][j] == 0:
                max_matrix[i][j] = max(max_matrix[i - 1][j] * -1, max_matrix[i - 1][j - 1] * -1, max_matrix[i - 1][j + 1] * -1, min_matrix[i - 1][j] * -1, min_matrix[i - 1][j - 1] * -1, min_matrix[i - 1][j + 1] * -1)
                min_matrix[i][j] = min(max_matrix[i - 1][j] * -1, max_matrix[i - 1][j - 1] * -1, max_matrix[i - 1][j + 1] * -1, min_matrix[i - 1][j] * -1, min_matrix[i - 1][j - 1] * -1, min_matrix[i - 1][j + 1] * -1)
            else:
                max_matrix[i][j] = max(max_matrix[i - 1][j] + matrix[i][j], max_matrix[i - 1][j - 1] + matrix[i][j], max_matrix[i - 1][j + 1] + matrix[i][j], min_matrix[i - 1][j] + matrix[i][j], min_matrix[i - 1][j - 1] + matrix[i][j], min_matrix[i - 1][j + 1] + matrix[i][j])
                min_matrix[i][j] = min(max_matrix[i - 1][j] + matrix[i][j], max_matrix[i - 1][j - 1] + matrix[i][j], max_matrix[i - 1][j + 1] + matrix[i][j], min_matrix[i - 1][j] + matrix[i][j], min_matrix[i - 1][j - 1] + matrix[i][j], min_matrix[i - 1][j + 1] + matrix[i][j])

print(max(max_matrix[-1]))
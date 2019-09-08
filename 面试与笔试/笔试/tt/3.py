import sys
dir = int(input().strip())
matrix = []
for i in range(4):
    matrix.append(list(map(int, sys.stdin.readline().strip().split(' '))))

if dir == 1:
    for i in range(0, 3):
        for j in range(0, 4):
            if matrix[i][j] == matrix[i+1][j]:
                matrix[i][j] *= 2
                matrix[i + 1][j] = 0
    for j in range(4):
        column = [0] * 4
        index = 0
        for i in range(0, 4):
            if matrix[i][j] != 0:
                column[index] = matrix[i][j]
                index += 1
        for i in range(0, 4):
            matrix[i][j] = column[i]
    for i in range(4):
        print(' '.join([str(x) for x in matrix[i]]))

if dir == 2:
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if matrix[i][j] == matrix[i-1][j]:
                matrix[i][j] *= 2
                matrix[i - 1][j] = 0

    for j in range(4):
        column = [0] * 4
        index = 0
        for i in range(3, -1, -1):
            if matrix[i][j] != 0:
                column[index] = matrix[i][j]
                index += 1
        for i in range(3, -1, -1):
            matrix[i][j] = column[3-i]
    for i in range(4):
        print(' '.join([str(x) for x in matrix[i]]))

if dir == 3:
    for i in range(0, 3):
        for j in range(0, 4):
            if matrix[j][i] == matrix[j][i+1]:
                matrix[j][i] *= 2
                matrix[j][i+1] = 0

    for j in range(4):
        column = [0] * 4
        index = 0
        for i in range(0, 4):
            if matrix[j][i] != 0:
                column[index] = matrix[j][i]
                index += 1
        for i in range(0, 4):
            matrix[j][i] = column[i]
    for i in range(4):
        print(' '.join([str(x) for x in matrix[i]]))

if dir == 4:
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if matrix[j][i] == matrix[j][i-1]:
                matrix[j][i] *= 2
                matrix[j][i-1] = 0

    for j in range(4):
        column = [0] * 4
        index = 0
        for i in range(3, -1, -1):
            if matrix[j][i] != 0:
                column[index] = matrix[j][i]
                index += 1
        for i in range(3, -1, -1):
            matrix[j][i] = column[3-i]
    for i in range(4):
        print(' '.join([str(x) for x in matrix[i]]))
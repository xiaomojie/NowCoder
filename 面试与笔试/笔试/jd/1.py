import sys
matrix = []
for i in range(5):
    line = list(map(int, sys.stdin.readline().strip().split(' ')))
    matrix.append(line)

count = 0
tmp = {}
for i in range(5):
    for j in range(5):
        if matrix[i][j] in tmp.keys():
            tmp[matrix[i][j]].append((i,j))
        else:
            tmp[matrix[i][j]] = [(i,j)]

count = 0
for key in tmp.keys():
    value = tmp[key]
    count1 = 0
    if len(value) < 3:
        count1 += len(value)
    count = 2
    val1 = sorted(value, key=lambda x:x[0])
    val2 = sorted(value, key=lambda x:x[1])
    max_len = 0
    # for val in value:
    #     if
    # count = 2

print(count)


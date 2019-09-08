import sys
n = int(input())
for k in range(n):
    line1 = list(map(int, sys.stdin.readline().strip().split(' ')))
    n = line1[0]
    # m = line1[1]
    matrix = []
    for i in range(n):
        matrix.append(sys.stdin.readline().strip())
    print(matrix)
    start = list(map(int, sys.stdin.readline().strip().split(' ')))
    end = list(map(int, sys.stdin.readline().strip().split(' ')))

    print(start, end)
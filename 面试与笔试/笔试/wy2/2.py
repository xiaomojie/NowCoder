import sys

T = int(input().strip())
for i in range(T):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    n = line[0]
    m = line[1]
    h = list(map(int,sys.stdin.readline().strip().split(" ")))
    total = (0 + n - 1) * n // 2
    if sum(h) + m < total:
        print("NO")
    else:
        print("YES")


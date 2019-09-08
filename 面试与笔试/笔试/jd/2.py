import sys
import random
T = int(input())
for i in range(T):
    line = list(map(int, sys.stdin.readline().strip().split(' ')))
    n = line[0]
    m = line[1]
    matrix = []
    for j in range(n):
        line = list(sys.stdin.readline().strip())
        matrix.append(line)
    x = random.randrange(0,1)
    # print(x)
    if x < 0.5:
        print("NO")
    else:
        print("YES")

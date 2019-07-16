import sys
n = int(sys.stdin.readline().strip())
res = []
p = []
for i in range(n):
    p.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(n):
    if p[i][0] == p[i][2]:  # 在列上
        low = min(p[i][1], p[i][3])
        high = max(p[i][1], p[i][3])
        if (low, p[i][0]) in res and (high, p[i][0]) in res:
            continue
        for j in range(low, high+1):
            if (j, p[i][0]) not in res:
                res.append((j, p[i][0]))
    else:  # 在行上
        low = min(p[i][0], p[i][2])
        high = max(p[i][0], p[i][2])
        if (p[i][1], low) in res and (p[i][1], high) in res:
            continue
        for j in range(low, high + 1):
            if (p[i][1], j) not in res:
                res.append((p[i][1], j))
print(len(res))
"""
3
1 2 3 2
2 5 2 3
1 4 3 4
"""
import sys

line = list(map(int, sys.stdin.readline().strip().split(" ")))
N = line[0]
M = line[1]
line = list(map(int, sys.stdin.readline().strip().split(" ")))

# i = 0
# j = M
# res = sum(line[i:j]) // M
res = 0
# while i < N-M + 1:
#     j = i + M
#     while j < N:
#         if sum(line[i:j]) / (j-i) > res:
#             res = sum(line[i:j]) / (j-i)
#         j += 1
#     i += 1
for i in range(0, N-M+1):
    for j in range(i+M-1, N):
        res = max(res, sum(line[i:j+1])/(j-i+1))


print("%.3f" %res)


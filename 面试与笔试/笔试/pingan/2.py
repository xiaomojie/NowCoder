import sys
import json

graph = json.loads(sys.stdin.readline().strip())
node = set()

for k, v in graph.items():
    node.add(k)
    node.update(v)

kd = {k: i for i, k in enumerate(node)}

matrix = [[0] * len(node) for i in range(len(node))]

for k, v in graph.items():
    for vv in v:
        matrix[kd[k]][kd[vv]] = 1
n = len(node)
visited = [0] * n
ans = False


def dfs(nums, i, flag):
    global n
    global ans
    for j in range(n):
        if nums[i][j] == 1 and flag[j] == 1:
            ans = True
            return
        elif nums[i][j] == 1 and flag[j] == 0:
            flag[j] = 1
            dfs(nums, j, flag)
            flag[j] = 0


for i in range(n):
    dfs(matrix, i, visited)

print(str(ans))
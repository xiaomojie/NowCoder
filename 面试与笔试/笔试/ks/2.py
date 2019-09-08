import sys
line = sys.stdin.readline().strip()
max_len = 0
start = 0
nearest = {}
for i in range(len(line)):
    if line[i] not in nearest.keys():
        nearest[line[i]] = i
    else:
        start = max(nearest[line[i]] + 1, start)
        max_len = max(max_len, i-start + 1)
        nearest[line[i]] = i

print(max_len)
import sys

n = int(input())
nums = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    a = line[0]
    t = line[1]
    nums.append([a,t])
nums.sort(key=lambda x:x[0], reverse=True)
v = 0
l = 0
for item in nums:
    l += (v * item[1] + 0.5 * item[0] * item[1] * item[1])
    v = v + item[0]*item[1]
print("%.1f" %l)

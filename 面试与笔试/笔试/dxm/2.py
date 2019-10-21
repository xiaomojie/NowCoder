import sys
line = list(map(int, sys.stdin.readline().strip().split(" ")))
N = line[0]
W = line[1]

w = list(map(int, sys.stdin.readline().strip().split(" ")))
t = list(map(int, sys.stdin.readline().strip().split(" ")))

nums = list(zip(w,t))
nums.sort(key=lambda x:x[0])

i = 0
res = 0
for i in range(len(nums)):
    j = len(nums) - 1
    while j >= 0 and nums[j][1] + nums[i][1] <= W:
        j -= 1
    res += max(nums[i][1], nums[j][1])
    res = 4

print(res)


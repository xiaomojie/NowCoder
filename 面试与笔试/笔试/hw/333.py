import sys
T = int(input())

for i in range(T):
    res = 0
    max_score = 0
    n = input()
    nums = list(map(int, sys.stdin.readline().strip().split(" ")))
    for j in range(1, len(nums)):
        for k in range(j - 1, -1, -1):
            if nums[k] > nums[j]:
                res -= 1
            elif nums[k] < nums[j]:
                res += 1
            else:

        max_score = max(max_score, res)
    print(max_score, res)
import sys
T = int(input())
for i in range(T):
    res = 0
    max_score = 0
    n = input()
    nums = list(map(int, sys.stdin.readline().strip().split(" ")))
    d = {nums[0]: 1}
    for j in range(1, len(nums)):
        tmp = sorted(d.items(), key=lambda x:x[0])
        for item in tmp:
            if item[0] < nums[j]:
                res += item[1]
            elif item[0] > nums[j]:
                res -= 1
        max_score = max(max_score, res)
        if nums[j] in d.keys():
            d[nums[j]] += 1
        else:
            d[nums[j]] = 1
    print(max_score, res)
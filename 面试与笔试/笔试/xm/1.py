import sys
def maxProfit(nums):
    if len(nums) <= 1:
        return 0
    res1, res2 = 0, 0
    tmp1, tmp2 = -nums[0], -nums[0]

    for i in nums[1:]:
        tmp1 = max(tmp1, -i)
        res1 = max(res1, tmp1 + i)
        tmp2 = max(tmp2, res1 - i)
        res2 = max(res2, tmp2 + i)
    return res2

# nums = list(map(int, sys.stdin.readline().strip().split(" ")))
# print(maxProfit(nums))


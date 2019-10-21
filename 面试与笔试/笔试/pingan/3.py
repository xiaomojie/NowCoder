import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))

def f(nums, n):
    avg = sum(nums) // n
    res = 0
    for i in range(len(nums)):
        if abs(nums[i] - avg) % 2 != 0:
            return -1
        if nums[i] > avg:
            res += (nums[i] - avg)//2
    return res

print(f(nums, n))
import sys

line = list(map(int, sys.stdin.readline().strip().split(" ")))
N = line[0]
M = line[1]
line = list(map(int, sys.stdin.readline().strip().split(" ")))


def maxSubArray(nums, M):
    if not nums:
        return 0
    maxSum = current = nums[0]
    count = 1
    for n in nums[1:]:
        if (current + n) / float(count + 1) > n:
            current = current + n
            count += 1
            if count > M:
                maxSum = max(maxSum, current / float(count))
        else:
            current = n
            count = 1
    return maxSum

print("%.3f" %maxSubArray(line, M))
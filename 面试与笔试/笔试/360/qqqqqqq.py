import sys

class Solution:
    def area(self, nums):
        M = len(nums)
        N = len(nums[0])
        res = 0
        for i in range(M):
            for j in range(N):
                res = res + nums[i][j] * 6
                if nums[i][j] > 1:
                    res = res - (nums[i][j] - 1) * 2
                if j > 0:
                    res = res - min(nums[i][j], nums[i][j - 1]) * 2
                if i > 0:
                    res = res - min(nums[i][j], nums[i - 1][j]) * 2
        return res


if __name__ == '__main__':

    line1 = list(map(int, sys.stdin.readline().strip().split(" ")))
    N = line1[0]
    input_matrix = []
    for i in range(N):
        line = list(map(int, sys.stdin.readline().strip().split(" ")))
        input_matrix.append(line)

    print(Solution().area(input_matrix))
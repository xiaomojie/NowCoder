import sys
class Solution:
    # 二分搜索法
    def binary_search(self, a, b):
        low = 0
        high = a
        while high - low > 1e-7:
            mid = (low + high) / 2
            if abs(pow(mid, b) - a) < 1e-7:
                return mid
            elif pow(mid, b) > a:
                high = mid
            else:
                low = mid
        return mid

# line = sys.stdin.readline().strip().split(" ")
# a = float(line[0])
# b = int(line[1])
# print(Solution().binary_search(a, b))
line = sys.stdin.readline().strip()
arr = list(map(int, line.split()))
a = arr[0]
b = arr[1]
print('%.6f' %Solution().binary_search(a, b))
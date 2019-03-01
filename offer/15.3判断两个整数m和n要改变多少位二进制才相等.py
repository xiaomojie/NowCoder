"""
输入两个整数m和n，计算需要改变m的二进制表示中的多少位才能得到n
"""
class Solution:
    def f(self, m, n):
    # 可以分两步进行，第一步先对m和n取异或，第二步算出异或结果中有多少个1
        p = m ^ n
        count = 0
        for i in range(32):
            if p & (1<<i):
                count += 1
        return count

print(Solution().f(10, 13))
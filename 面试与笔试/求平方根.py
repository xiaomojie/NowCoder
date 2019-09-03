# 求一个数的平凡根，可以使用牛顿迭代法和二分查找法

class Solution:
    # 二分搜索法
    def binary_search(self, num):
        low = 0
        high = num
        while high - low > 1e-7:
            mid = (low + high) / 2
            if abs(mid * mid - num) <= 1e-7:
                return mid
            elif mid * mid > num:
                high = mid
            else:
                low = mid
        return mid

    # 牛顿迭代法
    # f(x) = x^2 - n
    # 设r是f(x) = 0的根，选取x0作为r初始近似值，过点（x0,f(x0)）做曲线y = f(x)的切线L，L的方程为
    # y = f(x0)+f'(x0)(x-x0)，求出L与x轴交点的横坐标 x1 = x0-f(x0)/f'(x0)，称x1为r的一次近似值。
    # 过点（x1,f(x1)）做曲线y = f(x)的切线，并求该切线与x轴交点的横坐标 x2 = x1-f(x1)/f'(x1)，称
    # x2为r的二次近似值。重复以上过程，得r的近似值序列，其中x(n+1)=x(n)－f(x(n))/f'(x(n))，称为r的
    # n+1次近似值，上式称为牛顿迭代公式。
    # 则 x2 = x1 - (x1^2-n)/(2x1) = x1/2 + n/(2x1)
    def newton(self, num):
        k = 1
        while abs(k * k - num) > 1e-7:
            k = (k + num/k) / 2
        return k

print(Solution().binary_search(2))
print(Solution().newton(2))
print(Solution().binary_search(4))
print(Solution().newton(4))
print(Solution().binary_search(8))
print(Solution().newton(8))
print(Solution().binary_search(9))
print(Solution().newton(9))
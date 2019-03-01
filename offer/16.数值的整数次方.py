# -*- coding:utf-8 -*-
class Solution:
    def Power1(self, base, exponent):
        # 错误的法一：自以为简单的方法
        # 没有考虑指数为负数，没有考虑底数为0
        res = 1
        for i in range(exponent):
            res *= base
        return res

    invalid_input = False

    def Power(self, base, exponent):
        # 法二：全面但是不高效的方法
        res = 1
        if base == 0 and exponent <= 0:
            invalid_input = True
            return 0
        for i in range(abs(exponent)):
            res *= base
        if exponent < 0:
            res = 1/res
        return res
    def Power2(self, base, exponent):
        # 这种方法在python里面也出错，当exponent为负数的时候
        # 一个数的32次方等于16次方的平方
        # 当n为偶数时: a^n = a^(n/2) * a^(n/2)
        # 当n为奇数时：a^n = a^(n/2) * a^(n/2) * a
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.Power(base, exponent >> 1)
        res *= res
        if exponent & 1 == 1:
            res *= base
        return res

print(-2 >> 10)
print(Solution().Power(2.0, 3))
print(Solution().Power(-2.0, 3))
print(Solution().Power(2.0, -2))
print(Solution().Power(0, -3))
print(Solution().Power(0, 3))
print(Solution().Power(-2, -3))
print(Solution().Power(-3, 0))
print(Solution().Power(0, 0))
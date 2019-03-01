"""
题目：给你一根长度为n的绳子，请把绳子剪成m段(m、n都是整数，n>1并且m>1),每段绳子的长度记为k[0],k[1]...k[m]。请问每段绳子
的最大乘积是多少，例如当绳子长度为8时，把它剪成三段2/3/3，此时得到最大乘积18
"""

class Solution:
    def maxProductAfterCutting1(self, length):
        # 动态规划
        # 长度为n的绳子，在第一刀的时候有n-1种选择，设在i处剪，则f(n)=max(f(i)*f(n-i)) 0<i<n
        # 这是一个从上至下的递归，由于递归会有很多重复的子问题，所以按照自下而上的方法，先算f(2), f(3), f(4)等
        # 当n=2时，只能剪成两段（m>1）, f(2)=1; 当n=3时，f(3)=2,
        if length <= 0:
            return -1
        if 0 < length < 4:
            return length-1

        products = [0] * (length+1)
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, length+1):
            maxProduct = 0
            for j in range(1, i//2 + 1):
                maxProduct = max(products[j] * products[i-j], maxProduct)
                products[i] = maxProduct
        return products[length]

    def maxProductAfterCutting(self, length):
        # 贪婪算法
        # 当 n>= 5时，尽可能多的剪长度为3的绳子，当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子
        # 证明（反证法）：如果你剪绳子，剪了 N 段，假设这时候，这N个数相乘为最大，且存在一个数a
        # 大于等于5，那么 这个数 a 分解成为 3 x (a-3)  比原来的结果更大，所以前面相乘结果不是最大的
        # 所以使得N个数相乘为最大，则不存在大于等于5的一段
        # 书上：2(n-2)>n    3(n-3)>n   &  3(n-3) >= 2(n-2) 所以尽可能分成3的段
        if length <= 0:
            return -1
        if 0 < length < 4:
            return length-1
        # 尽可能多减去长度为3的绳子段
        timesOf3 = length//3
        # 当最后剩下的长度为4时，不能再减去长度为3的绳子段
        # 此时更好的方法是剪成2个两段的
        if length - timesOf3 * 3 == 1:
            timesOf3 -= 1

        timeOf2 = (length - timesOf3 * 3) // 2
        return pow(3, timesOf3) * pow(2, timeOf2)


print(Solution().maxProductAfterCutting(8))
print(Solution().maxProductAfterCutting(0))
print(Solution().maxProductAfterCutting(1))
print(Solution().maxProductAfterCutting(2))
print(Solution().maxProductAfterCutting(3))
print(Solution().maxProductAfterCutting(4))


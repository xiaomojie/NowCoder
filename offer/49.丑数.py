"""
只包含因子2/3/5的数为丑数，求从小到大第1500个丑数是什么
"""
"""
思路一：逐一判断是否是丑数，直到1500个
思路二：生成1500个丑数，后面的每一个丑数肯定是当前丑数集合中的某一个数乘以2或3或5得到的
"""
class Solution:
    def isUgly(self, num):
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num /3
        while num % 5 == 0:
            num /= 5
        return num == 1

    def GetUglyNumber_Solution(self, index):
        count = 0
        num = 0
        while count < index:
            num += 1
            if self.isUgly(num):
                count += 1
        return num


class Solution2:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        count = 1
        ugly = [1]*index
        lastugly2 = 0
        lastugly3 = 0
        lastugly5 = 0
        while count < index:
            ugly[count] = min(ugly[lastugly2] * 2, ugly[lastugly3] * 3, ugly[lastugly5] * 5)
            while ugly[lastugly2] * 2 <= ugly[count]:
                lastugly2 += 1
            while ugly[lastugly3] * 3 <= ugly[count]:
                lastugly3 += 1
            while ugly[lastugly5] * 5 <= ugly[count]:
                lastugly5 += 1
            count += 1
        return ugly[count-1]

# print(Solution2().GetUglyNumber_Solution(1))
print(Solution2().GetUglyNumber_Solution(2))
print(Solution2().GetUglyNumber_Solution(3))
print(Solution2().GetUglyNumber_Solution(4))
print(Solution2().GetUglyNumber_Solution(5))
print(Solution2().GetUglyNumber_Solution(6))
print(Solution2().GetUglyNumber_Solution(7))
print(Solution2().GetUglyNumber_Solution(8))
print(Solution2().GetUglyNumber_Solution(9))
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1_1(self, n):
        # 是一种有问题的解法
        # python中并没有对int类型的位数进行限制
        # 但是对于有符号数，例如为负数的时候，统计会出错，因为负数右移左边添加的是1
        # 例如输入-1，输出为32
        # count = 0
        # for i in range(32):
        #    count +=  (n >> i)&1
        # return count
        return sum([(n >> i & 1) for i in range(32)])

    def NumberOf1(self, n):
        # 法二：为了避免上面的问题，采取对1进行移位
        # 这种方法需要循环32位
        count = 0
        for i in range(32):
            if n & (1 << i):
                count += 1
        return count

    def NumberOf1_2(self, n):
        # 法三：这种算法n中有几个1则需要循环几次
        # 也报错
        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count


print(Solution().NumberOf1(-1))
print(Solution().NumberOf1(-127))
# print(Solution().NumberOf1(10))
# print(Solution().NumberOf1(8))
# print(Solution().NumberOf1(15))
# print(Solution().NumberOf1(1232132))

print(bin(-1))

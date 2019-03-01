class Solution:
    # 如果一个整数是2的整数次方，那么他的二进制表示中有且只有移位是1，其他为都为0
    # 将这个整数减去1，再和你自身进行&运算，则得到0
    def f(self, num):
        if not (num-1)&num:
            return True
        else:
            return False

print(Solution().f(16))
print(Solution().f(15))
print(Solution().f(1024))
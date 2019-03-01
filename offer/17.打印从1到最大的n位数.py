"""
输入数字n，按顺序打印出从1到最大的n位十进制数，比如输入3，则打印出1,2,3一直到最大的3位数999
"""
class Solution:
    def pring_1_to_max_of_digits1(self, n):
        # 法一：直接打印，可能会遇到大数问题，当n很大的时候
        if n <= 0:
            return
        num = 1
        for i in range(n):
            num *= 10
        for i in range(num):
            print(i)
    def pring_1_to_max_of_digits(self, n):
        # 法二：数字排列解法
        if n <= 0:
            return
        num = [0]*n
        self.pring_1_to_max_of_digits_recursively(num, n, 0)

    def pring_1_to_max_of_digits_recursively(self, num, n, index):
        if index == n:
            self.print_num(num)
            return
        for i in range(10):
            num[index] = str(i)
            self.pring_1_to_max_of_digits_recursively(num, n, index+1)

    def print_num(self, num):
        print(''.join(num).lstrip('0'))

Solution().pring_1_to_max_of_digits(3)
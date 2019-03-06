# -*- coding:utf-8 -*-
"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。

类似题目：二叉搜索树的前序遍历结果
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.VerifySquenceOfBSTRecursion(sequence)

    def VerifySquenceOfBSTRecursion(self, sequence):
        if not sequence:
            return True
        root = sequence[-1]
        i = 0
        while i < len(sequence) - 1:
            if sequence[i] < root:
                i += 1
            else:
                break
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False

        return self.VerifySquenceOfBSTRecursion(sequence[:i]) and self.VerifySquenceOfBSTRecursion(sequence[i:-1])

print(Solution().VerifySquenceOfBST([5,7,6,9,11,10,8]))
print(Solution().VerifySquenceOfBST([5,7,6]))
print(Solution().VerifySquenceOfBST([7,4,6,5]))
print(Solution().VerifySquenceOfBST([4,8,6,12,16,14,10]))
print(Solution().VerifySquenceOfBST([]))
print(Solution().VerifySquenceOfBST([1]))
print(Solution().VerifySquenceOfBST([1,2,3,4]))
print(Solution().VerifySquenceOfBST([4,3,2,1]))
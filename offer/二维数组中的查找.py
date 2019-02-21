"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上
到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find1(self, target, array):
        # 法一：暴力搜索 O(m*n)
        for i in range(len(array)):
            for j in range(len(array[0])):
                if target == array[i][j]:
                    return True
        return False
    def Find2(self, target, array):
        # 法二：对每行进行二分搜索，O(nlogm)
        for i in range(len(array)):
            l, r = 0, len(array[i])-1
            while l <= r:
                mid = (l+r)//2
                if array[i][mid] == target:
                    return True
                elif array[i][mid] < target:
                    l = mid + 1
                else: 
                    r = mid - 1
        return False

    def Find(self, target, array):
        # 法三：矩阵是有序的，可以从左下角A（或右上角）出发，若target小于A，
        # 则必定在上方的行，若大于则必定在右侧的列
        if not array or len(array) == 0:
            return False
        i = len(array)-1
        j = 0
        while i >= 0 and j < len(array[0]):
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                j += 1
            else:
                i -= 1
        return False
    
    # 思路四：把整个矩阵分成四个块A,B,C,D，左上角的块A中的元素始终小于右下角块D中
    # 的元素，以A中最右下角的元素a作为基准，比较a与target的大小，若a > target,则
    # 在上方或者左方找（A,B,C中，A有重叠），若小于则在下方或右方找（B,C,D中，D有重
    # 叠），但是这样的查找给我们带来了不便，因为每次比较完之后，下次要查找的区域有重叠，
    # 而且没有规律。

print(Solution().Find(1,None))
print(Solution().Find(1,[]))
print(Solution().Find(1,[[]]))
print(Solution().Find(1,[[0,2,3],[2,4,6]]))

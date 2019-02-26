# -*- coding:utf-8 -*-
"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的
数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，
该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # 本体的数组在一定程度上是有序的，可以考虑使用二分查找，但是特别要注意一些
        # 特例情况，设置头指针s和尾指针e：
        # 1. 如果中间元素m位于前半段，则它应该大于等于第一个元素，将s指向m
        # 2. 如果中间元素m位于后半段，则它应该小于等于最后一个元素，将e指向m
        # 按照上面思路，s总是指向前面递增数组的元素，e总是指向后面递增数组的元素，
        # 最终他们会指向相邻的元素，此时e指向的则为最小。
        # 特例：
        # a. 把排序数组的前面0个元素放到后面，此时最小为第一个
        # b. 数组中存在相同的元素，当s，e，m相等的时候，就无法判断最小值到底是在
        # 前半段还是后半段了，此时不得不采用顺序查找的方法
        # 顺序查找O(n),二分查找O(logn)
        if len(rotateArray) == 0:
            return 0
        s, e = 0, len(rotateArray) - 1
        m = s  # 为了特例a
        while rotateArray[s] >= rotateArray[e]:
            if e - s == 1:
                m = e
                break
            m = (s + e) // 2
            if rotateArray[m] == rotateArray[s] == rotateArray[e]:
                return self.MinInOrder(rotateArray, s, e)
            if rotateArray[m] >= rotateArray[s]:
                s = m
            elif rotateArray[m] <= rotateArray[e]:
                e = m
        return rotateArray[m]

    def MinInOrder(self, rotateArray, s, e):
        res = 0
        while s <= e:
            if res > rotateArray[s]:
                res = rotateArray[s]
            s += 1
        return res


print(Solution().minNumberInRotateArray([]))
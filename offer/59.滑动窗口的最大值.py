# -*- coding:utf-8 -*-

"""
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗
口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}，
 {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""

'''
思路：使用一个额外的双向开口的队列来保存最大值
队列存最大值：如果当前要存入的大于队尾，则队尾弹出，直到不小于当前，然后当前入列；如果小于，则直接加入队尾
'''
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or len(num) < size or size < 1:
            return []
        max_queue = []
        res = []
        for i in range(len(num)):
            # if not max_queue:
            #     max_queue.append(num[i])
            # elif num[i] > max_queue[-1]:
            #     while max_queue and num[i] > max_queue[-1]:
            #         max_queue.pop()
            #     max_queue.append(num[i])
            # else:
            #     max_queue.append(num[i])

            # 上面的可以直接用下面三行代替
            while max_queue and num[i] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(num[i])

            if i < size - 1:
                continue
            else:
                res.append(max_queue[0])
                if max_queue[0] == num[i - size + 1]:
                    max_queue = max_queue[1:]
        return res



# print(Solution().maxInWindows([6,6,6,6,6,7],2))
# print(Solution().maxInWindows([10,14,12,11],0))
# print(Solution().maxInWindows([10,14,12,11],1))
print(Solution().maxInWindows([16,14,12,10,8,6,4],5))
print(Solution().maxInWindows([1,3,5,7,9,11,13,15],4))
print(Solution().maxInWindows([2,3,4,2,6,2,5,1], 3))

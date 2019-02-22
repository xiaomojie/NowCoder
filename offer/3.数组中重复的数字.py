"""
## 注意不一定存在重复
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是
重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组
{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate1(self, numbers, duplication):
        # 法一：使用内置函数Counter
        c=collections.Counter(numbers)
        for k, v in c.items():
            if v > 1:
                duplication[0] = k
                return True
        return False
    def duplicate2(self, numbers, duplication):
        # 法二：不使用内置函数，修改数组 时间O(n),空间O(1)
        i = 0
        while i < len(numbers):
            if numbers[i] == i:
                i += 1
                continue
            tmp = numbers[numbers[i]]
            if numbers[i] == tmp:
                duplication[0] = tmp
                return True
            else:
                numbers[numbers[i]] = numbers[i]
                numbers[i] = tmp
        return False
    def duplicate(self, numbers, duplication):
        # 法三：修改数组,利用现有数组设置标志，当一个数字被访问过后，可以设置
        # 对应位上的数 + n，之后再遇到相同的数时，会发现对应位上的数已经大于
        # 等于n了，那么直接返回这个数即可
        n = len(numbers)
        for i in range(n):
            index = numbers[i]
            if index >= n:
                index -= n
            if numbers[index] >= n:
                duplication[0] = index
                return True
            numbers[index] += n
        return False
    # 其他思路：
    # 1. 先排序，时间O(nlogn)
    # 2. 利用额外的哈希表存储，将元素放到哈希表对应的下标，时间O(n),空间O(n)
print(Solution().duplicate([2,1,3,1,4],[]))
print(Solution().duplicate([2,3,1,0,2,5,3],[]))

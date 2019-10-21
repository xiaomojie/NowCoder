"""
首先将数组中的元素转化成字符串的形式，以便直接进行拼接。可以看到，输出结果就是对原来的数组元素进行排序之后，再连接输出。但是，这里不能用传统的单纯比较大小的规则，这里需要重新定义一个比较大小的规则：
若ab > ba 则 a > b，
若ab < ba 则 a < b，
若ab = ba 则 a = b；
因此，可以利用这个规则，对转换成字符串的数组进行排序，并连接起来。
因此，我们可以在快排中修改排序规则，利用修改之后的快排对字符进行排序。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 自定义排序规则加快排
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0:
            return ""
        numbers = map(str, numbers)
        pivot = numbers[0]
        less = [i for i in numbers[1:] if (pivot+i)>(i+pivot)]
        great = [i for i in numbers[1:] if (pivot+i)<=(i+pivot)]
        result = "".join(self.PrintMinNumber(less))+pivot+"".join(self.PrintMinNumber(great))
        return result.lstrip("0")


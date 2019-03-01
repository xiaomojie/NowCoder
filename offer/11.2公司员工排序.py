"""
实现一个排序算法，要求时间效率为O(n)，对公司员工的年龄进行排序（员工数量几万人，
其实是在一个小范围内进行排序），只允许使用常量大小的辅助空间，不能超过O(n)
"""
class Solution:
    def sort(self, nums):
        if not nums or len(nums) == 0:
            return nums
        count_of_age = [0] * 99
        for i in range(len(nums)):
            if 1 <= nums[i] <= 99:
                count_of_age[nums[i]] += 1
            else:
                print("age out of range")
        index = 0
        for i in range(99):
            for j in range(count_of_age[i]):
                nums[index] = i
                index += 1

ages = [1,2,3,1,3,4,2,4,5,6,3]
Solution().sort(ages)
print(ages)

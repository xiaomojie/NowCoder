# time: O(n^2)
class Solution:
    def bubble_sort1(self, num):
        for i in range(len(num)-1):
            for j in range(len(num) - 1 - i):
                if num[j] > num[j+1]:
                    num[j], num[j+1] = num[j+1], num[j]
        return num

    def bubble_sort(self, num):
        i = len(num)-1
        while i > 0:
            last_change = 0
            for j in range(i):
                if num[j] > num[j+1]:
                    num[j], num[j+1] = num[j+1], num[j]
                    last_change = j
            i = last_change
        return num




# num = [49, 38, 65, 97, 76, 13, 27, 49]
# num = [1,2,3,1,3,4,2,4,5,6,3]
num = [1,2,3,4,5,6]
print(Solution().bubble_sort(num))
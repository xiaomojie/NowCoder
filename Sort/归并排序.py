#
class Solution:
    def merge(self, left, right):
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:] or right[j:]
        return res

    def sort(self, num):
        if not num or len(num) <= 1:
            return num
        mid = len(num) >> 1
        left = self.sort(num[:mid])
        right = self.sort(num[mid:])
        res = self.merge(left, right)
        return res

print(Solution().sort(None))
print(Solution().sort([]))
print(Solution().sort([1]))
print(Solution().sort([1,2,3,4]))
print(Solution().sort([4,3,2,1,0]))
print(Solution().sort([49,38,65,97,76,13,27]))
print(Solution().sort([49,38,65,97,76,13]))

a = [1,2]
def d(a):
    a[0], a[1] = a[1], a[0]
d(a)
print(a)


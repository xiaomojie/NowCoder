class Solution:
    def odd(self, n):
        for i in n:
            if i % 2 == 0:
                return False
        return True

    def even(self, n):
        for i in n:
            if i % 2 != 0:
                return False
        return True
    def smallest(self, n):
        if self.even(n) or self.odd(n):
            return n
        n.sort()
        return n

if __name__=='__main__':
    s = Solution()
    n = input()
    num = list(map(int, input().split(' ')))


    res = s.smallest(num)
    for each in res:
        print(each, end=' ')
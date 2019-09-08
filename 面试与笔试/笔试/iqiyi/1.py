import sys
n = int(input().strip())
a = list(map(int, sys.stdin.readline().strip().split(' ')))


class Solution:
    def Permutation(self, ss):
        # write code here
        res = []
        if ss == '':
            return res

        ss = list(ss)
        self._Permutation(ss, 0, res)

        count = 0
        for tmp in res:
            flag = True
            for i in range(len(a)):
                if a[i] == 1 and tmp[i] <= tmp[i+1]:
                    flag = False
                    break
                elif a[i] == 0 and tmp[i] >= tmp[i+1]:
                    flag = False
                    break
            if flag:
                count += 1

        return count

    def _Permutation(self, ss, begin, res):
        if begin == len(ss) - 1:
            res.append(''.join(ss))
            return

        for i in range(begin, len(ss)):
            if ss[begin] == ss[i] and begin != i:
                continue
            ss[begin], ss[i] = ss[i], ss[begin]
            self._Permutation(ss, begin + 1, res)
            ss[begin], ss[i] = ss[i], ss[begin]

count = Solution().Permutation(''.join([str(x) for x in range(1,n+1)]))
print(count%1000000007)
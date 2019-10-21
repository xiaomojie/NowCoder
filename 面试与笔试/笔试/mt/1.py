import sys

class Solution:
    def max_value(self, easy, hard):
        if len(easy) == 0:
            return 0
        elif len(easy) == 1:
            return easy[0]
        else:
            res = [0]*len(easy)
            res[0] = easy[0]
            res[1] = max(easy[0] + easy[1], hard[1])
            for i in range(2, len(easy)):
                res[i] = max(res[i-1] + easy[i], res[i-2] + hard[i])
            return res[-1]

N = int(input().strip())
easy = []
hard = []
for i in range(N):
    line = list(map(float, sys.stdin.readline().strip().split(" ")))
    easy.append(line[0])
    hard.append(line[1])
print(Solution().max_value(easy, hard))
import sys

class Solution:
    def f(self, g,n,m):
        if n < 0.9:
            return 0
        out = 0.0
        out += g*(n/(n+m))
        g = g*(m/(n+m))
        m -= 1

        if m < 0.9:
            return out
        g = g * (m / (n + m))
        m -= 1
        out = out + self.f(g, n, m-1)*(m/(n+m))+self.f(g, n-1, m)*(n/(n+m))
        return out

a = list(map(int, sys.stdin.readline().strip().split(' ')))
n = a[0]
red = n
m = a[1]
blue = m
out = Solution().f(1,n,m)

print("%.5f" %out)
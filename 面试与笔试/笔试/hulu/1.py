import sys

line = list(map(int, sys.stdin.readline().strip().split(' ')))
n = line[0]
m = line[1]
a = list(map(int, sys.stdin.readline().strip().split(' ')))
w = list(map(int, sys.stdin.readline().strip().split(' ')))

def last_remain(n, m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(2, n+1):
        last = (last + m) % i
    return last
last = last_remain(n, m)

prob = 0
sum_w = sum(w)
for j in range(n):
    for i in range(n):
        if a[i] == 1 and ((i-j)+n)%n == last:
            prob += w[j]/sum_w
print('%.5f' %prob)

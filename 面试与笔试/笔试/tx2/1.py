from collections import Counter
import sys
# a = [1,1,2,3]
n = int(input())
for i in range(n):
    input()
    a = list(map(int, sys.stdin.readline().strip().split(' ')))
    d = Counter(a)
    res = sorted(d.items(), key=lambda x:x[1], reverse=True)
    if res[0][1] > len(a)//2:
        print("NO")
    else:
        print("YES")

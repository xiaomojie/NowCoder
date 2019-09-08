import copy

nn = int(input())
ss = input()
temp = ss.split()


def evaluate(l):
    ss = ''.join(l)
    return eval(ss)


for ii in range(nn):
    for jj in range(nn - 1):
        t = copy(temp)
        if int(temp[2 * jj]) > int(temp[2 * jj + 2]):
            t[2 * jj], t[2 * jj + 2] = t[2 * jj + 2], t[2 * jj]
            if evaluate(t) == evaluate(temp):
                temp = t

print(' '.join(temp))


import sys
n = int(input().strip())
s = sys.stdin.readline().strip().split(' ')

i = 0
num = []
op = []
while i < len(s) and i + 1 < len(s):
    num.append(s[i])
    op.append(s[i+1])
    i += 2
num.append(s[i])

res = []
tmp = []
pre = ""
for i in range(len(op)):
    if i == 0:
        tmp.append(num[i])
        pre = op[i]
    else:
        if op[i] == "+" or op[i] == "-":
            if pre == "+" or pre == "-":
                tmp.append(num[i])
            else:
                tmp.append(num[i])
                res += sorted(tmp, key=lambda x: int(x))
                tmp = []
            pre = op[i]
        else:
            if pre == "*" or pre == "/":
                tmp.append(num[i])
            else:
                res += sorted(tmp, key=lambda x: int(x))
                tmp = []
                tmp.append(num[i])

            pre = op[i]

tmp.append(num[-1])
res += sorted(tmp, key=lambda x: int(x))
j = i = 0
while i < len(op):
    res = res[:j+1] + [op[i]] + res[j+1:]
    j += 2
    i += 1
print(' '.join(res))



"""
6
3 + 2 + 1 + -4 * -5 + 1


3
1 + 2 + 3

7
3 + 2 + 1 + -4 * -5 * 1 + 2

3
1 + 3 / 2

5
3 * 4 / 2 + 5 * 1

1
3

2
2 * 1

4
1 + 3 * 2 * 1

4
1 - 6 - 5 + 4
"""




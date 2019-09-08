import sys
def yinshu(x):
    fac = [x]
    for i in range(2, x):
        if x % i == 0:
            fac.append(i)
            continue
        else:
            pass
    # if len(fac) == 0:
    #     return []
    # else:
    return fac

# print(yinshu(2))
# print(yinshu(3))
# print(yinshu(4))
# print(yinshu(6))
# print(yinshu(8))
# print(yinshu(9))

n = int(input().strip())
num = list(map(int, sys.stdin.readline().strip().split(' ')))
fac = []
for x in num:
    fac.append(yinshu(x))

print(fac)
res = [[1, list(set(fac[0]))]]
for i in range(1, len(fac)):
    for j in range(len(res)):
        if len(list(set(res[j][1]).intersection(set(fac[i])))):
            # print(res[j][1])
            # print(set(res[j][1]).union(set(fac[i])))
            print(list(set(res[j][1]).union(set(fac[i]))))
            res[j][1] = list(set(res[j][1]).union(set(fac[i])))
            res[j][0] += 1
            print(fac)
        else:
            res.append((1, set(fac[i])))
print(res)

for i in range(len(res)):
    for j in range(i+1, len(res)):
        if len(res[i][1]) and set(res[i][1]).intersection(set(res[j][1])):
            res[i][1] = list(set(res[i][1]).union(set(res[j][1])))
            res[i][0] += 1
            res[j][0] = 0
            res[j][1] = []

count = 0
for i in range(len(res)):
    if res[i][0]:
        count += 1
print(count)

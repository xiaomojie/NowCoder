n = int(input().strip())
m = int(input().strip())
s = []
for i in range(m):
    s.append(input().strip())

i = 0
res = []
p = []
v = []
flag = True
while i < len(s):
    if flag and not s[i].startswith("P"):
        res.append(s[i])
    else:
        flag = False
        if s[i].startswith("P"):
            p.append(s[i])
        else:
            v.append(s[i])
    i += 1

# print(p,v)

if not len(p):
    print(res)
else:
    i = 0
    j = 0
    aa = 0
    while i < len(p) and j < len(v):
        res.append(p[i])
        count = n - 1
        k = j
        while count > 0 and j < len(v):
            res.append(v[j])
            count -= 1
            j += 1
        else:
            if j != len(v):
                j -= 1
        i += 1
        j += 1
        aa = count
    else:
        if j >= len(v) and aa == 0 and i < len(p):
            res.append(p[i])
        elif i >= len(p):
            res += v[j:]
        # if aa == 0:
        #     if i >= len(p):
        #         res += v[j:]
        #     else:
        #         res.append(p[i])


print(len(res))
for i in range(len(res)):
    print(res[i])



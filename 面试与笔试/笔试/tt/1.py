import sys
n = int(input().strip())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().strip().split(' '))))

d = {}
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] >= 3:
            if i not in d.keys():
                d[i] = [j]
            else:
                d[i].append(j)

if len(d.keys()) == 1:
    print(n - len(d[list(d.keys())[0]]))
else:
    # new_keys = d.keys()
    remove = []
    for key in d.keys():
        if key not in remove:
            val = d[key]
            add = []
            for tmp in val:
                if tmp in d.keys():
                    add += d[tmp]
                    remove.append(tmp)
            add = list(set(add))
            d[key] += add
    for tmp in remove:
        d.pop(tmp)
    count = len(d.keys())
    all = []
    for tmp in d.keys():
        all.append(tmp)
        all += d[tmp]
    all = list(set(all))
    count += n - len(all)
    print(count)
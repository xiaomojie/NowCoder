import sys
T = int(input().strip())
for i in range(T):
    line = list(map(int, sys.stdin.readline().strip().split(" ")))
    tmp = []
    for j,x in enumerate(line):
        tmp.append((j,x))
    tmp.sort(key=lambda x:x[1], reverse=True)
    res = [0] * 3
    for j in range(len(tmp)):
        if tmp[j][1] % 2 == 0:
            div1 = div2 = tmp[j][1] / 2
        else:
            div1 = tmp[j][1] // 2
            div2 = tmp[j][1] // 2 + 1
        # tmp[-1][0] tmp
    print((sum(line) + 2)//3 )


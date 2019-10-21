import sys
input()
line = list(map(int, sys.stdin.readline().strip().split(" ")))
line = [-1] + line
count = 0
i = 1

while i < len(line):
    if line[i] <= 0:
        i += 1
        continue

    tmp1 = 1
    if i*2 < len(line) and line[i*2] > 0:
        tmp1 += 1
    if i*2+1 < len(line) and line[i*2+1] > 0:
        tmp1 += 1

    tmp2 = 0
    if i%2 == 0 and i/2 >= 0:
        tmp2 += 1
        if i+1 < len(line) and line[i+1] > 0:
            tmp2 += 1

    tmp3 = 0
    if (i-1) % 2 == 0 and (i-1)/2 >= 0:
        tmp3 += 1
        if (i-1) >= 0 and line[i-1] > 0:
            tmp3 += 1

    if max(tmp1, tmp2, tmp3) == tmp1:
        line[i] -= 1
        if i*2 < len(line):
            line[i*2] -= 1
        if i * 2 + 1 < len(line):
            line[i*2+1] -= 1
    elif max(tmp1, tmp2, tmp3) == tmp2:
        line[i] -= 1
        if i+1 < len(line):
            line[i+1] -= 1
    else:
        line[i] -= 1
        if i - 1 < len(line):
            line[i-1] -= 1

    count += 1
    if line[i] <= 0:
        i += 1

print(count)



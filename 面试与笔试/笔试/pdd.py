import sys
line = list(sys.stdin.readline().strip().split(";"))
num = list(map(int, line[0].split(",")))
k = int(line[1])

odd = []
even = []

for x in num:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

even.sort(reverse=True)
odd.sort(reverse=True)

if len(even) >= k:
    print(",".join([str(x) for x in even[:k]]))
else:
    print(",".join([str(x) for x in even + odd[0:k-len(even)]]))
